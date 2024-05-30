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
class BandGapCurve:
    
    def __init__(self) -> None:
        self.supply = N670x(Instruments().ID.PowerSupply)
        self.chamber = su_241(Instruments().ID.TempChamber)
        self.multimeter = mul_34401A(Instruments().ID.Multimeter1)
        # reset power supply Vbat, VDDIO, and Realy VCC
        self.supply.setVoltage(channel=1,voltage=0)
        self.supply.setVoltage(channel=2,voltage=0)
        self.supply.setVoltage(channel=3,voltage=0)
        # sleep(0.3)
        self.supply.setVoltage(channel=1,voltage=4)
        self.supply.setVoltage(channel=2,voltage=3.3)
        self.supply.setVoltage(channel=3,voltage=5)
        sleep(2)
        log.info('........... BandGap ........')
        self.mcp = MCP2221()
        self.mcp.ConfigGPIO0(True)
        self.mcp.GPIO0(True)
        sleep(1)
        Startup(mcp=self.mcp)
        # sleep(2)
        self.mcp.GPIO0(False)
        # sleep(0.5)
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
        input('>')
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
            for temp in tqdm(range(30,140,10)):
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
                sleep(100)
                for i in tqdm(range(0,16,1)):
                    value = self.mcp.mcpRead(SlaveAddress=0x6c, data=[0xB1])[0]
                    log.warning(hex(value))
                    value = ((value & 0x0f)| (i<<4))
                    log.warning(hex(value))
                    self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0xB1,value])
                    sleep(0.3)
                    setCode.append(i)
                    BandGapValue.append(self.multimeter.meas_V())
                    # erro_percentage.append((abs(BandGapValue[-1]) - 1.799)/BandGapValue[-1] *100)
                #Reset the Chip and Vddio powersupply
                if not os.path.exists(Path('measurements/BandGapCurve/Device1')):
                    os.makedirs(Path('measurements/BandGapCurve/Device1'))
                data = pd.DataFrame({'SetCode':setCode,'BandGapValue':BandGapValue})
                data.to_csv(f'measurements/BandGapCurve/Device1/BandgapCurve_{temp}C.csv')



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


        
BandGapCurve()