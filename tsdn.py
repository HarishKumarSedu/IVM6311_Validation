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
class TSDN:
    
    def __init__(self) -> None:
        self.supply = N670x(Instruments().ID.PowerSupply)
        self.supply.setVoltage(channel=1,voltage=4)
        self.supply.setVoltage(channel=3,voltage=5)
        self.multimeter = mul_34401A(Instruments().ID.Multimeter1)
        sleep(4)
        log.info('........... Tsdn ........')
        self.mcp = MCP2221()
        self.mcp.ConfigGPIO0(True)
        self.mcp.GPIO0(True)
        sleep(0.5)
        Startup(mcp=self.mcp)
        sleep(0.5)
        self.mcp.GPIO0(False)
        EnableAnalogTestPoint(mcp=self.mcp)
        TsdnInstructions = [ 
            [0xFE,0x01],
            [0x19,0x81],
            [0x1A,0x04],
            # [0xB0,0x0E],
            [0xB3,0x00],
        ]
        for instruction in TsdnInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        
        if self.mcp.mcpRead(SlaveAddress=0x6c, data=[0x1A]):
            log.info('Tsdn Brought in SWDN pin ....!')
            log.warning(self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0]))
            
            self.measure_Tsdn()
        else:
            log.error('Tsdn Brought Signal error re-run procedure ....!')
        
        self.resetSetUp()
    
    def measure_Tsdn(self):
        setCode = []
        TsdnValue = []
        erro_percentage = []
        setabsCode = []
        for i in tqdm(range(0,8)):
            value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB3])[0]
            log.warning(hex(value))
            value = (value&0x1f | (i<<5))
            setabsCode.append(hex(value))
            log.warning(hex(value))
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB3,value])
            sleep(0.3)
            setCode.append(i)
            TsdnValue.append(self.multimeter.meas_V())
        # self.resetSetUp()
            # erro_percentage.append((abs(TsdnValue[-1]) - 1.799)/TsdnValue[-1] *100)
        if not os.path.exists(Path('measurements/Tsdn')):
            os.makedirs(Path('measurements/Tsdn/'))
        data = pd.DataFrame({'SetCode':setCode,'TsdnValue':TsdnValue,'setabsCode':setabsCode})
        data['error_percentage']  = data['TsdnValue'].apply(lambda x : abs(((x-0.542)/1.799)*100))
        # data.to_csv('measurements/Tsdn/Tsdn1.csv')
        
        trimmingCode_index = data[['error_percentage']].idxmin()
        optimal_value = data.loc[trimmingCode_index,"TsdnValue"].to_list()[-1]
        
        log.warning(f'Optimal value : {optimal_value}V')
        log.warning(f'min value : {data.loc[trimmingCode_index,"SetCode"].to_list()[-1]}')

    def resetSetUp(self):
        #Reset the Chip and Vddio powersupply
        self.mcp.GPIO0(True)
        sleep(0.3)
        self.mcp.reset()
        sleep(0.3)
        self.supply.setVoltage(channel=1,voltage=0)
        sleep(0.3)
        self.supply.setVoltage(channel=1,voltage=4)
        self.supply.setVoltage(channel=2,voltage=0)
        sleep(0.3)
        self.supply.setVoltage(channel=2,voltage=3.3)
if __name__ == '__main__':
    tsdn = TSDN()
    