# from IvmDriver.mcp2221 import MCP2221
from mcp2221 import MCP2221
from procedures.startup import Startup
from procedures.Enable_Ana_Testpoint import EnableAnalogTestPoint
from IvmDriver.logger import log
from KeySight_N670x import N670x
from Instruments.multimeter import mul_34401A
from TempChamber import su_241
# power supply id 
# USB0::0x0957::0x0F07::MY50000622::INSTR
from time import sleep 
from common import Instruments
import pandas as pd 
from tqdm import tqdm
import os 
from pathlib import Path
class BandGap:
    
    def __init__(self) -> None:
        self.supply = N670x(Instruments().ID.PowerSupply)
        self.chamber = su_241(Instruments().ID.TempChamber)
        self.multimeter = mul_34401A(Instruments().ID.Multimeter1)
        # reset power supply Vbat, VDDIO, and Realy VCC
        self.supply.setVoltage(channel=1,voltage=0)
        self.supply.setVoltage(channel=2,voltage=0)
        self.supply.setVoltage(channel=3,voltage=0)
        sleep(0.3)
        self.supply.setVoltage(channel=1,voltage=4)
        self.supply.setVoltage(channel=2,voltage=3.3)
        self.supply.setVoltage(channel=3,voltage=5)
        sleep(2)
        log.info('........... BandGap ........')
        self.mcp = MCP2221()
        self.mcp.ConfigGPIO0(True)
        self.mcp.GPIO0(True)
        sleep(0.5)
        Startup(mcp=self.mcp)
        self.mcp.GPIO0(False)
        # sleep(1)
        EnableAnalogTestPoint(mcp=self.mcp)
        BandGapInstructions = [ 
            [0xFE,0x01],
            [0x19,0x81],
            [0x1A,0x01],
            [0xB0,0x0E],
        ]
        for instruction in BandGapInstructions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
            sleep(0.3)
        # input('>')
        # let the Analog Voltage settle down for while 
        # sleep(0.5)
        if self.mcp.mcpRead(SlaveAddress=0x6c, data=[0x1A]):
            log.info('BandGap Brought in SWDN pin ....!')
            log.warning(self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0]))
            self.measure_BandGap()
        else:
            log.error('BandGap Brought Signal error re-run procedure ....!')
        
    
    def measure_BandGap(self):
        try:
            for temp in tqdm(range(130,-50,-10)):
                setCode = []
                BandGapValue = []
                erro_percentage = []
                Temperature = []
                if temp == 130:
                    temp = 125
                self.chamber.set_temp(temp=temp)

                log.warning(f'Set Temperature {temp}:> Chamber temperature {self.chamber.read_temp()}')
                while ( float(temp) !=    (temperature := self.chamber.read_temp())):
                    log.warning(f'Reading temperature from chamber:> {temperature}')
                    sleep(10)
                    ...
                sleep(300)
                for i in tqdm(range(15,7,-1)):
                    value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[0]
                    # log.warning(hex(value))
                    value = ((value & 0x0f)| (i<<4))
                    # log.warning(hex(value))
                    self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB0,value])
                    sleep(0.3)
                    setCode.append(i)
                    BandGapValue.append(self.multimeter.meas_V())
                    erro_percentage.append((abs(BandGapValue[-1]) - 1.799)/BandGapValue[-1] *100)
                for i in tqdm(range(8)):
                    value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[0]
                    log.warning(hex(value))
                    value = ((value & 0x0f)| (i<<4))
                    log.warning(hex(value))
                    self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB0,value])
                    sleep(0.3)
                    setCode.append(i)
                    BandGapValue.append(self.multimeter.meas_V())
                    # erro_percentage.append((abs(BandGapValue[-1]) - 1.799)/BandGapValue[-1] *100)
                #Reset the Chip and Vddio powersupply
                if not os.path.exists(Path('measurements/TempBandgap1')):
                    os.makedirs(Path('measurements/TempBandgap1/'))
                data = pd.DataFrame({'SetCode':setCode,'BandGapValue':BandGapValue})
                data['error_percentage']  = data['BandGapValue'].apply(lambda x : abs(((x-1.799)/1.799)*100))
                data.to_csv(f'measurements/TempBandgap1/Bandgap_{temp}C.csv')

                trimmingCode_index = data[['error_percentage']].idxmin()
                optimal_value = data.loc[trimmingCode_index,"BandGapValue"].to_list()[-1]

                if  1.793 < optimal_value <1.804:
                    log.warning(f'Optimal value : {optimal_value}V')
                    log.warning(f'min value : {data.loc[trimmingCode_index,"SetCode"].to_list()[-1]}')
                else:
                    log.error(f'Trimming failed measured value : {optimal_value} ')
            # for temp in tqdm(range(-10,-50,-10)):
            #     setCode = []
            #     BandGapValue = []
            #     erro_percentage = []
            #     Temperature = []
            #     if temp == 130:
            #         temp = 125
            #     self.chamber.set_temp(temp=temp)

            #     log.warning(f'Set Temperature {temp}:> Chamber temperature {self.chamber.read_temp()}')
            #     while ( float(temp) !=  self.chamber.read_temp()):
            #         log.warning(f'Reading temperature from chamber:> {self.chamber.read_temp()}')
            #         ...
            #     sleep(300)
            #     for i in tqdm(range(15,7,-1)):
            #         value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[0]
            #         # log.warning(hex(value))
            #         value = ((value & 0x0f)| (i<<4))
            #         # log.warning(hex(value))
            #         self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB0,value])
            #         sleep(0.3)
            #         setCode.append(i)
            #         BandGapValue.append(self.multimeter.meas_V())
            #         erro_percentage.append((abs(BandGapValue[-1]) - 1.799)/BandGapValue[-1] *100)
            #     for i in tqdm(range(8)):
            #         value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB0])[0]
            #         log.warning(hex(value))
            #         value = ((value & 0x0f)| (i<<4))
            #         log.warning(hex(value))
            #         self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB0,value])
            #         sleep(0.3)
            #         setCode.append(i)
            #         BandGapValue.append(self.multimeter.meas_V())
            #         # erro_percentage.append((abs(BandGapValue[-1]) - 1.799)/BandGapValue[-1] *100)
            #     #Reset the Chip and Vddio powersupply
            #     if not os.path.exists(Path('measurements/TempBandgap')):
            #         os.makedirs(Path('measurements/TempBandgap/'))
            #     data = pd.DataFrame({'SetCode':setCode,'BandGapValue':BandGapValue})
            #     data['error_percentage']  = data['BandGapValue'].apply(lambda x : abs(((x-1.799)/1.799)*100))
            #     data.to_csv(f'measurements/TempBandgap/Bandgap_{temp}C.csv')

            #     trimmingCode_index = data[['error_percentage']].idxmin()
            #     optimal_value = data.loc[trimmingCode_index,"BandGapValue"].to_list()[-1]

            #     if  1.793 < optimal_value <1.804:
            #         log.warning(f'Optimal value : {optimal_value}V')
            #         log.warning(f'min value : {data.loc[trimmingCode_index,"SetCode"].to_list()[-1]}')
            #     else:
            #         log.error(f'Trimming failed measured value : {optimal_value} ')
            self.mcp.GPIO0(True)
            sleep(0.3)
            self.mcp.reset()
            sleep(0.3)
            self.supply.setVoltage(channel=1,voltage=0)
            self.supply.setVoltage(channel=2,voltage=0)
            self.supply.setVoltage(channel=3,voltage=0)
            sleep(0.3)
            self.supply.setVoltage(channel=1,voltage=4)
            self.supply.setVoltage(channel=2,voltage=3.3)
            self.supply.setVoltage(channel=3,voltage=5)
        except KeyboardInterrupt:
            self.mcp.GPIO0(True)
            sleep(0.3)
            self.mcp.reset()
            sleep(0.3)
            self.supply.setVoltage(channel=1,voltage=0)
            self.supply.setVoltage(channel=2,voltage=0)
            self.supply.setVoltage(channel=3,voltage=0)
            sleep(0.3)
            self.supply.setVoltage(channel=1,voltage=4)
            self.supply.setVoltage(channel=2,voltage=3.3)
            self.supply.setVoltage(channel=3,voltage=5)


        
BandGap()