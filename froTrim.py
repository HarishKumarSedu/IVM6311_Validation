# from IvmDriver.mcp2221 import MCP2221
from mcp2221 import MCP2221
from procedures.startup import Startup
from IvmDriver.logger import log
from KeySight_N670x import N670x
from Instruments.DigitalScope import dpo_2014B
from time import sleep 
from common import Instruments
import pandas as pd 
from tqdm import tqdm
import os 
from pathlib import Path
from tqdm import tqdm
class FROTrim:
    
    def __init__(self,mcp) -> None:
        # self.supply = N670x(Instruments().ID.PowerSupply)
        self.scope = dpo_2014B(Instruments().ID.DigitalScope)
        # self.supply.setVoltage(channel=1,voltage=0)
        # self.supply.setVoltage(channel=2,voltage=0)
        # self.supply.setVoltage(channel=4,voltage=0)
        # self.supply.setVoltage(channel=3,voltage=0)
        # sleep(0.3)
        # self.supply.setVoltage(channel=1,voltage=4)
        # self.supply.setVoltage(channel=3,voltage=5)
        sleep(2)
        log.info('........... FRO Trimming ........')
        # self.mcp = MCP2221()
        self.mcp = mcp 
        # self.mcp.ConfigGPIO0(True)
        # self.mcp.GPIO0(False)
        sleep(2)
        # Startup(mcp=self.mcp)
        self.trimregister = 0xEF
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
            [self.trimregister,0xE7],


        ]
        for instruction in FroInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.5)
        self.fro_Values__Sweep()
    def fro_Values__Sweep(self):
        self.measure_values=[]
        self.trim_code=[]
        self.error_abs=[]
        self.typical = 13*(10**6)
        # self.scope.set_autoSet()
        self.scope.set_trigger__mode(mode='NORM')
        self.scope.set_HScale()
        self.scope.set_Channel__VScale(scale=0.5)
        # self.scope.init_scopePosEdge__Trigger(channel='CH1')
        sleep(1)
        for value in tqdm(range(0,2**(5),1)):
            self.mcp.mcpWrite(SlaveAddress=0x6c,data=[self.trimregister,(0xE0+value)])
            sleep(0.5)
            freq = 0
            # input('>>>>>>>>')
            for _ in range(0,10):
                freq= freq + self.scope.meas_Freq()
            self.measure_values.append(freq/10) # get the frequency values from scope
            # print(f'Frequency ====> {freq}')
            self.error_abs.append(abs(self.measure_values[-1]/(10**6) - 13))
            self.trim_code.append(value)
            log.debug(f'Trimming code : {self.trim_code[-1]}')
            log.debug(f'Trimming Fro Value : {self.measure_values[-1]}')
        self.fro_Limit__Check()
    def fro_Limit__Check(self):
        
        error_min = min(self.error_abs)
        error_min__Index =self.error_abs.index(error_min)
        # if error_min < 0.5:
        log.info(f'Measured Value : {self.measure_values[error_min__Index]}')
        self.trimcode = self.trim_code[error_min__Index]
        log.info(f'Trim code : {self.trimcode}')
        # self.burn_value(trimcode=trimcode)
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[self.trimregister,(0xE0 | self.trimcode)])
        self.trim_codeValue()
    def trim_codeValue(self):
        return [self.trimregister, self.mcp.mcpRead(SlaveAddress=0x6c, data=[self.trimregister])[-1]]
    
    def burn_value(self, trimcode):
        # self.supply.setVoltage(channel=2,voltage=8)
        # self.supply.setVoltage(channel=4,voltage=14)
        # self.supply.outp_ON(channel=2)
        # self.supply.outp_ON(channel=4)
        sleep(4)
        BandgapBurn_Instruction = [
        [0xFE,0x0],
        [0xB0,0xFE],
        [0xFE,0x1],
        [self.trimregister,(0x03 << 5 | trimcode)],
        [0xAF,0xBF],
        [0xAE,0x02],
        [0xAE,0x00],
        ]
        for instruction in BandgapBurn_Instruction:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(1)
        BandgapValue =self.mcp.mcpRead(SlaveAddress=0x6c,data=[0xB0], Nobytes=1)[-1]
        if BandgapValue == (0x0E << 5 | trimcode):
            log.info(f'Band Trim Value {BandgapValue} burned Successfully ...!')
        else:
            log.critical(f'Bandgap Trim vlaue not able to burn ...!')
        sleep(2)
        # self.supply.outp_OFF(channel=2)
        # self.supply.outp_OFF(channel=4)

if __name__ == '__main__':
    FROTrim()