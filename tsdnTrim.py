# from IvmDriver.mcp2221 import MCP2221
from mcp2221 import MCP2221
from procedures.startup import Startup
from procedures.Enable_Ana_Testpoint import EnableAnalogTestPoint
from IvmDriver.logger import log
from KeySight_N670x import N670x
from Instruments.multimeter import mul_34401A
# power supply id 
# USB0::0x0957::0x0F07::MY50000622::INSTR
from time import sleep 
from common import Instruments
import pandas as pd 
from tqdm import tqdm
import os 
from pathlib import Path
class TSDNTrim:
    
    def __init__(self,mcp) -> None:
        # self.supply = N670x(Instruments().ID.PowerSupply)
        # self.supply.setVoltage(channel=2,voltage=3.3)
        self.multimeter = mul_34401A(Instruments().ID.Multimeter1)
        log.info('........... Tsdn ........')
        self.mcp = mcp
        # self.mcp.GPIO0(True)
        # sleep(3)
        # Startup(mcp=self.mcp)
        # sleep(3)
        # self.mcp.GPIO0(False)
        EnableAnalogTestPoint(mcp=self.mcp)
        self.trimregister = 0xB3
        TsdnInstructions = [ 
            [0xFE,0x01],
            [0x19,0x81],
            [0x1A,0x04],
            [0xB0,0x0E],
            [self.trimregister,0x00],
        ]
        for instruction in TsdnInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        # input('>')
        if self.mcp.mcpRead(SlaveAddress=0x6c, data=[0x1A]):
            log.info('Tsdn Brought in SWDN pin ....!')
            self.measure_Tsdn()
        else:
            log.error('Tsdn Brought Signal error re-run procedure ....!')
    
    def measure_Tsdn(self):
        setCode = []
        TsdnValue = []
        erro_percentage = []
        setabsCode = []
        for i in tqdm(range(0,8)):
            value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[self.trimregister])[0]
            value = (value&0x1f | (i<<5))
            setabsCode.append(hex(value))
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=[self.trimregister,value])
            sleep(0.3)
            setCode.append(i)
            TsdnValue.append(self.multimeter.meas_V())

        data = pd.DataFrame({'SetCode':setCode,'TsdnValue':TsdnValue,'setabsCode':setabsCode})
        data['error_percentage']  = data['TsdnValue'].apply(lambda x : abs(((x-0.542)/1.799)*100))
        
        trimmingCode_index = data[['error_percentage']].idxmin()
        optimal_value = data.loc[trimmingCode_index,"TsdnValue"].to_list()[-1]
        
        log.warning(f'Optimal value : {optimal_value}V')
        self.trimcode = data.loc[trimmingCode_index,"SetCode"].to_list()[-1]
        log.warning(f'min value : {self.trimcode}')
        self.trim_codeValue()
    def trim_codeValue(self):
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[self.trimregister,self.trimcode << 4 | 0xE])
        log.warning(hex(self.trimcode << 4 | 0xE))
        return [self.trimregister,self.mcp.mcpRead(SlaveAddress=0x6c, data=[self.trimregister])[-1]]

if __name__ == '__main__':
    tsdn = TSDNTrim()
    