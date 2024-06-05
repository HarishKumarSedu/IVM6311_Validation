
from froTrim import FROTrim
from tsdnTrim import TSDNTrim
from KeySight_N670x import N670x
from common import Instruments
from mcp2221 import MCP2221
from time import sleep
from procedures.startup import Startup
from bandgapTrim import BandgapTrim
from IvmDriver.logger import log
from Instruments.Keysight_E362x import E362X
import os 
from datetime import datetime
import json
from e3648 import E3648
class MainTrim:
    def __init__(self) -> None:
        self.supply1 = E3648(port=Instruments().ID.KesightSupply1)
        self.supply2 = E3648(port=Instruments().ID.KesightSupply2)
        self.supply1.setCurrent(channel=1,current=0.5)
        self.supply1.setCurrent(channel=2,current=1)
        self.supply2.setRange(channel=1,range=1)
        self.supply2.setRange(channel=2,range=1)
        self.supply1.setVoltage(channel=1,voltage=4)
        self.supply1.setVoltage(channel=2,voltage=5)
        self.supply2.setVoltage(channel=1,voltage=4) # vbso 8v 
        self.supply2.setVoltage(channel=2,voltage=4) #vbias 14v
        self.supply2.setCurrent(channel=1,current=0.5)
        self.supply2.setCurrent(channel=2,current=0.5)
        # self.supply = N670x(Instruments().ID.PowerSupply)
        # self.supply.setVoltage(channel=1,voltage=4)
        # self.supply.setVoltage(channel=2,voltage=4)
        # self.supply.setVoltage(channel=4,voltage=4)
        # self.supply.setVoltage(channel=3,voltage=5)
        # self.supply.outp_ON(channel=1)
        # self.supply.outp_ON(channel=2)
        # self.supply.outp_ON(channel=3)
        # self.supply.outp_ON(channel=4)
        sleep(2)
        self.mcp = MCP2221()
        self.trimvalues = []
        self.mcp.GPIO0(True)
        self.mcp.ConfigGPIO0(True)
        sleep(1)
        Startup(mcp=self.mcp)
        sleep(1)
        self.mcp.GPIO0(False)
        sleep(2)
        bandgap = BandgapTrim(mcp=self.mcp)
        self.trimvalues.append(bandgap.trim_codeValue())
        for instruction in self.trimvalues:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        tsdn = TSDNTrim(mcp=self.mcp)
        self.trimvalues.append(tsdn.trim_codeValue())
        for instruction in self.trimvalues:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        fro = FROTrim(mcp=self.mcp)
        self.trimvalues.append(fro.trim_codeValue())
        for instruction in self.trimvalues:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        print(f'trim values {self.trimvalues}')
        self.burn_values()
        self.mcp.reset()
        # self.supply.setVoltage(channel=1,voltage=0)
        # self.supply.setVoltage(channel=3,voltage=0)
        # self.supply.setVoltage(channel=2,voltage=0)
        # self.supply.setVoltage(channel=4,voltage=0)
        # self.supply.outp_OFF(channel=1)
        # self.supply.outp_OFF(channel=2)
        # self.supply.outp_OFF(channel=3)
        # self.supply.outp_OFF(channel=4)
        self.supply1.setVoltage(channel=1,voltage=0)
        self.supply1.setVoltage(channel=2,voltage=0)
        self.supply2.setVoltage(channel=1,voltage=0) # vbso 8v 
        self.supply2.setVoltage(channel=2,voltage=0) #vbias 14v
        self.supply2.setCurrent(channel=1,current=0)
        self.supply2.setCurrent(channel=2,current=0)

    def burn_values(self):
        # self.supply.setVoltage(channel=2,voltage=8)
        # self.supply.setVoltage(channel=4,voltage=14)
        self.supply2.setCurrent(channel=1,current=0.5)
        self.supply2.setCurrent(channel=2,current=0.5)
        self.supply2.setVoltage(channel=1,voltage=8) # vbso 8v 
        self.supply2.setVoltage(channel=2,voltage=14) #vbias 14v
        sleep(3)
        burn_registers = [
        [0x0F,0x80],
        [0xFE,0x00],
        [0xB0,0xFE],
        [0xFE,0x01],
        [0xB1,0x1F],
        [0xAF,0x00],
        [0xAE,0x02],
        [0xAE,0x00],
        ]
        for instruction in burn_registers:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xFE,0x00])
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x00,0x01])
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x00,0x00])
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xFE,0x01])
        for instruction in self.trimvalues:
            if self.mcp.mcpRead(SlaveAddress=0x6c, data=[instruction[0]])[-1] == instruction[1]:
                log.info(f'Reg {hex(instruction[0])} - {hex(instruction[1])} Passed')
            else:
                log.critical(f'Reg {hex(instruction[0])} -----x----- {hex(instruction[1])} Failed')
            sleep(0.3)
        with open(f'trimvalues/chip_data.json','r') as file:
            data = json.load(file)
            data.append(self.trimvalues)
        with open(f'trimvalues/chip_data.json','w') as file:
            json.dump(data,file )
        print(hex(self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[-1]))
        

if __name__ == '__main__':
    MainTrim()