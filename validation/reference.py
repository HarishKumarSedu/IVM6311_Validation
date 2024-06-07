# from IvmDriver.mcp2221 import MCP2221
from IVM6311_Validation.mcp2221 import MCP2221
from IVM6311_Validation.procedures.startup import Startup
from IVM6311_Validation.procedures.Enable_Ana_Testpoint import EnableAnalogTestPoint
from IvmDriver.logger import log
from Instruments.KeySight_N670x import N670x
from Instruments.multimeter import mul_34401A
from time import sleep 
from common import Instruments
import pandas as pd 
from tqdm import tqdm
import os 
from pathlib import Path

class Reference:
    
    def __init__(self) -> None:
        self.meter = mul_34401A(Instruments().ID.Multimeter34410A)
        # sleep(2)
        log.info('........... BandGap ........')
        self.mcp =  MCP2221()
        sleep(2)
        Startup(mcp=self.mcp)
        input('Remove Reset on SDWN pin >')
        EnableAnalogTestPoint(mcp=self.mcp)
        BandGapInstructions = [ 
            [0xFE,0x01],
            [0x19,0x81],
            [0x1A,0x01],
        ]
        for instruction in BandGapInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            # sleep(0.3)
        if data := self.mcp.mcpRead(SlaveAddress=0x6c, data=[0x1A]):
            self.measure_UVLO()
            log.info(f'Everything is fine {data} ....:)')
        else:
            log.critical('Error in Bring Analog Reference ....!')
        
    
    def measure_UVLO(self):
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x00])
        sleep(2)
        log.info(f'Uvlo voltage {self.meter.meas_V()}')
    def measure_LDORef(self):
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x05])
        sleep(2)
        log.info(f'Bandgap voltage {self.meter.meas_V()}')

if __name__ == '__main__':
    Reference()