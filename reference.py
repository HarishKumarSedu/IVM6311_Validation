from froTrim import FROTrim
from tsdnTrim import TSDNTrim
from common import Instruments
from mcp2221 import MCP2221
from time import sleep
from procedures.startup import Startup
from procedures.Enable_Ana_Testpoint import EnableAnalogTestPoint
from bandgapTrim import BandgapTrim
from IvmDriver.logger import log
from Instruments.Keysight_E362x import E362X
from Instruments.Keysight_34461 import A34461
from Instruments.DigitalScope import dpo_2014B
import os 
from datetime import datetime
import json
from e3648 import E3648
from tqdm import tqdm
import pandas as pd
from TempChamber import su_241

from AzComp import AzComp

class Reference :

    def __init__(self,chipid=1,temp=25) -> None:
        self.chamber = su_241(Instruments().ID.TempChamber)
        # self.supply1 = E3648(port=Instruments().ID.KesightSupply1)
        self.supply1 = E3648(port=Instruments().ID.KesightSupply2)
        self.multimeter1 = A34461(Instruments().ID.Multimeter2)
        self.multimeter2 = A34461(Instruments().ID.Multimeter34410A)
        self.scope = dpo_2014B(Instruments().ID.DigitalScope)
        self.supply1.setVoltage(channel=1,voltage=0)
        self.supply1.setVoltage(channel=2,voltage=0)
        sleep(2)
        self.supply1.setCurrent(channel=1,current=0.5)
        self.supply1.setCurrent(channel=2,current=1)
        self.supply1.setVoltage(channel=1,voltage=4)
        self.supply1.setVoltage(channel=2,voltage=5)
        sleep(2)
        self.temperature = temp
        self.mcp = MCP2221()
        self.mcp.ConfigGPIO0(True)
        self.mcp.GPIO0(True)
        sleep(1)
        Startup(mcp=self.mcp)
        # sleep(1)
        self.mcp.GPIO0(False)
        # sleep(5)
        input('Remove the SDWN reset : > ')
        EnableAnalogTestPoint(mcp=self.mcp)
        # self.chamber.set_temp(temp=temp)
        # while ( float(temp) !=    (temperature := self.chamber.read_temp())):
        #     log.warning(f'Reading temperature from chamber:> {temperature}')
        #     sleep(20)
        #     ...
        # sleep(300)
        
        log.warning(f'Set Temperature {temp}:> Chamber temperature {self.chamber.read_temp()}')
        self.meas_references(chipid)
        self.chamber.set_temp(temp=25)

    def meas_references(self, id):
        # Startup(mcp=self.mcp)
        # self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xFE,0x01]) 
        # self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x0F,0x88]) 
        # self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x17,0x00]) 
        # self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x18,0x00]) 
        if self.temperature == 25:
            file = 'reference25'
            AzCompfile = 'AzComp25'
        if self.temperature == 80:
            file = 'reference80'
            AzCompfile = 'AzComp25'
        if self.temperature == -40:
            file = 'reference_m40'
            AzCompfile = 'AzComp_m40'
        log.critical(f'file folder: {file} , {AzCompfile}')
        bandgap_Instructions = [ 
        [0xFE,0x01],
        [0x19,0x81],
        [0x1A,0x01],
        ]
        for instruction in bandgap_Instructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.1)
        sleep(2)
        bandgap=self.multimeter1.meas_V()
        print(f'Bandgap voltage : {bandgap}')
        # input('>')
        vvco_Instructions = [ 
        [0x1A,0x02],
        ]
        for instruction in vvco_Instructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.1)
        sleep(2)
        VVCO=self.multimeter1.meas_V()
        print(f'VVCO voltage : {VVCO}')
        sleep(2)
        ldoa_Instructions = [ 
        [0xFE,0x01],
        [0x19,0x81],
        [0x1A,0x05],
        ]
        for instruction in ldoa_Instructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.1)
        LDOA=self.multimeter1.meas_V()
        print(f'LDOA {LDOA}')
        fro_Instructions = [ 
            [0xFE,0x00],
            [0x00,0x01],
            [0xFE,0x01],
            [0x2F,0xAA],
            [0x2F,0xBB],
            [0x03,0x01],
            [0x04,0x25],
            # [0x0F,0x80],
            # [0xB0,0x1E],
        ]
        for instruction in fro_Instructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.1)
        # input('>')
        self.scope.set_trigger__mode(mode='NORM')
        self.scope.set_HScale()
        self.scope.set_Channel__VScale(scale=0.5)
        sleep(2)
        freq=0
        for i in range(0,10):
            freq= freq + self.scope.meas_Freq()
            sleep(1)
        freq = freq/10
        # freq=self.scope.meas_Freq()
        print(f'Fro Frequency : {freq}')
        print('Change Multimeter +ve probe from SDWN to VDD :>')
        self.mcp.ConfigGPIO0(True)
        sleep(3)
        DVDLDO = self.multimeter1.meas_V()
        print(f'DVDLDO : {DVDLDO}V')
        ############################AzComp Test ####################
        AzComp(mcp=self.mcp, chipid=id, file=AzCompfile)
        ###########################################################
        voltage=2.5
        while (UVLOHL := self.multimeter2.meas_V()) >= 1.5:
             sleep(0.1)
             self.supply1.setVoltage(channel=1,voltage=voltage)
             voltage=voltage-0.01
        UVLOHL=voltage
        print(f'UVLOHL {UVLOHL}V')
        input('Put reset SDWN back :>')
        voltage=1
        self.supply1.setVoltage(channel=1,voltage=voltage)
        while UVLOLH := self.multimeter2.meas_V() <= 1.1:
             sleep(0.1)
             self.supply1.setVoltage(channel=1,voltage=voltage)
             voltage=voltage+0.01
             if voltage > 3:
                 break
        UVLOLH=voltage
        print(f'UVLOHL {UVLOLH}V')
        os.makedirs(f'measurements/Char/{file}',exist_ok=True)
        if not os.path.exists(f'measurements/Char/{file}/reference2.json'):
            with open(f'measurements/Char/{file}/reference2.json', 'w') as file:
                json.dump({},file)
        with open(f'measurements/Char/{file}/reference2.json', 'r') as file :
            data = json.load(file)
            if str(id) not in data:
                data.update({
                    id:{
                        'bandgap':bandgap,
                        'VVCO':VVCO,
                        'LDOA':LDOA,
                        'fro':freq,
                        'DVDLDO':DVDLDO,
                        'UVLOHL':UVLOHL,
                        'UVLOLH':UVLOLH,
                    }
                })
                with open(f'measurements/Char/reference_m40/reference2.json', 'w', encoding='utf8') as file :
                    json.dump(data,file)
            else:
                log.warning(f'chip id {id} data already exits')

    def uvlo(self):
        voltage=2.5
        while (UVLOHL := self.multimeter2.meas_V()) >= 1.5:
             sleep(0.1)
             self.supply1.setVoltage(channel=1,voltage=voltage)
             voltage=voltage-0.01
        UVLOHL=voltage
        print(f'UVLOHL {UVLOHL}V')
        print('Put reset SDWN back :>')
        voltage=1
        self.supply1.setVoltage(channel=1,voltage=voltage)
        while UVLOLH := self.multimeter2.meas_V() <= 1.1:
             sleep(0.1)
             self.supply1.setVoltage(channel=1,voltage=voltage)
             voltage=voltage+0.01
             if voltage > 3:
                 break
        UVLOLH=voltage
        print(f'UVLOHL {UVLOLH}V')

def excel_convert():
    with open('measurements/Char/reference25/reference1.json', 'r') as file :
        data = json.load(file)
        pd.DataFrame(data=data).to_csv('measurements/Char/reference25/reference@80.csv')
if __name__ == '__main__':
    # for temp in [80,-40,25]:
    #     reference = Reference(chipid=1, temp=temp)
    # excel_convert()
    reference = Reference(chipid=1, temp=-40)

