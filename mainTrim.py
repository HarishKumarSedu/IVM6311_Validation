
from froTrim import FROTrim
from tsdnTrim import TSDNTrim
from KeySight_N670x import N670x
from common import Instruments
from mcp2221 import MCP2221
from time import sleep
from procedures.startup import Startup
from bandgapTrim import BandgapTrim
from IvmDriver.logger import log
import os 
from datetime import datetime
import json

class MainTrim:
    def __init__(self) -> None:
        
        self.supply = N670x(Instruments().ID.PowerSupply)
        self.supply.setVoltage(channel=1,voltage=4)
        self.supply.setVoltage(channel=2,voltage=4)
        self.supply.setVoltage(channel=4,voltage=4)
        self.supply.setVoltage(channel=3,voltage=5)
        self.supply.outp_ON(channel=1)
        self.supply.outp_ON(channel=2)
        self.supply.outp_ON(channel=3)
        self.supply.outp_ON(channel=4)
        sleep(6)
        self.mcp = MCP2221()
        self.trimvalues = []
        self.mcp.ConfigGPIO0(True)
        self.mcp.GPIO0(True)
        sleep(15)
        Startup(mcp=self.mcp)
        sleep(5)
        self.mcp.GPIO0(False)
        # sleep(1)
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
        self.supply.setVoltage(channel=1,voltage=0)
        self.supply.setVoltage(channel=3,voltage=0)
        self.supply.setVoltage(channel=2,voltage=0)
        self.supply.setVoltage(channel=4,voltage=0)
        self.supply.outp_OFF(channel=1)
        self.supply.outp_OFF(channel=2)
        self.supply.outp_OFF(channel=3)
        self.supply.outp_OFF(channel=4)

    def burn_values(self):
        self.supply.setVoltage(channel=2,voltage=8)
        self.supply.setVoltage(channel=4,voltage=14)
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