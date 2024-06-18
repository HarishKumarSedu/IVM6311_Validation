
from common import Instruments
from mcp2221 import MCP2221
from froTrim import FROTrim
from time import sleep
from procedures.startup import Startup
from procedures.Enable_Ana_Testpoint import EnableAnalogTestPoint
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

class FROCheck :

    def __init__(self,chipid=1,temp=25) -> None:
        self.chamber = su_241(Instruments().ID.TempChamber)
        self.supply1 = E3648(port=Instruments().ID.KesightSupply2)
        self.multimeter = A34461(Instruments().ID.Multimeter2)
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
        sleep(1)
        Startup(mcp=self.mcp)
        input('Remove the SDWN reset : > ')
        EnableAnalogTestPoint(mcp=self.mcp)
        BandGapInstructions = [ 
            [0xFE,0x01],
            # [0x19,0x81],
            [0x1A,0x01],
            [0xB1,0x00],
            [0xB0,0x0E],
        ]
        for instruction in BandGapInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        
        FroInstructions = [ 
            # [0xFE,0x00],
            # [0x00,0x0D], 
            # [0xFE,0x01],
            # [0x03,0x01],
            # [0x04,0x25],
            # [0xB0,0x0E],
            # [0x0F,0x80],
            [0xFE,0x00],
            [0x00,0x01],
            [0xFE,0x01],
            [0x2F,0xAA],
            [0x2F,0xBB],
            [0x03,0x01],
            [0x04,0x25],
            [0x0F,0x80],
            [0xEF,0xF7],
        ]
        for instruction in FroInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.5)
        for temp in [-40,35,50,80,90]:
            self.chamber.set_temp(temp=temp)
            log.warning(f'Set Temperature {temp}:> Chamber temperature {self.chamber.read_temp()}')
            while ( float(temp) !=    (temperature := self.chamber.read_temp())):
                log.warning(f'Reading temperature from chamber:> {temperature}')
                sleep(100)
                ...
            sleep(100)
            # if temp == 25:
            #     froTrim = FROTrim(mcp=self.mcp)
            #     log.info(f'fro Trim code: {froTrim.trim_codeValue()}')
            fro=self.scope.meas_Freq()
            BandGapValue = []
            for i in tqdm(range(8)):
                value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[0]
                value = ((value & 0x0f)| (i<<4))
                sleep(0.1)
                self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB0,value])
                sleep(0.3)
                BandGapValue.append(self.multimeter.meas_V(count=1))
            for i in tqdm(range(15,7,-1)):
                value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[0]
                value = ((value & 0x0f)| (i<<4))
                sleep(0.1)
                self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB0,value])
                sleep(0.3)
                BandGapValue.append(self.multimeter.meas_V(count=1))
            with open(f'measurements/Char/FRO/froChar.json', 'r') as file :
                data = json.load(file)
                if str(temperature) not in data:
                    data.update({
                        str(temperature):{
                            'fro':fro
                        }

                    })
                    with open(f'measurements/Char/FRO/froChar.json', 'w') as file :
                        json.dump(data,file)
                else:
                    log.warning(f'chip temperature {temperature} data already exits')

            with open(f'measurements/Char/FRO/bandgap.json', 'r') as file :
                data = json.load(file)
                if str(temperature) not in data:
                    data.update({
                        str(temperature):{
                            'bandgap':BandGapValue
                        }

                    })
                    with open(f'measurements/Char/FRO/bandgap.json', 'w') as file :
                        json.dump(data,file)
                else:
                    log.warning(f'chip temperature {temperature} data already exits')
if __name__ == '__main__':
    FROCheck()