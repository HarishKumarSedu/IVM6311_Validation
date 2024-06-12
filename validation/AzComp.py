# from IvmDriver.mcp2221 import MCP2221
from IVM6311_Validation.mcp2221 import MCP2221
from IVM6311_Validation.procedures.startup import StartupAzComp
from IVM6311_Validation.procedures.Enable_Ana_Testpoint import EnableAnalogTestPoint
from IvmDriver.logger import log
from KeySight_N670x import N670x
from multimeter import mul_34401A
from time import sleep 
from common import Instruments
import pandas as pd 
from tqdm import tqdm
import os 
from pathlib import Path
import json

class AzComp:
    
    def __init__(self,chipid=1) -> None:
        self.PowerSupply = N670x(Instruments().ID.PowerSupply)
        self.Multimeter34410A = mul_34401A(Instruments().ID.Multimeter34410A)
        log.info('........... AzComp Measurement ........')
        self.mcp =  MCP2221()
        sleep(2)
        StartupAzComp(mcp=self.mcp)
        input('Remove Reset on SDWN pin >')
        EnableAnalogTestPoint(mcp=self.mcp)
        AzCompInstrunctions = [ 
            [0xFE,0x01],
            [0x19,0x88],
        ]
        for instruction in AzCompInstrunctions:
            self.mcp.mcpWrite(SlaveAddress=0x6c, data=instruction)
        input('>')
        if data := self.mcp.mcpRead(SlaveAddress=0x6c, data=[0x1A]):
            self.Azcomp_tests(chipid)
            log.info(f'Everything is fine {data} ....:)')
        else:
            log.critical('Error in Bring Analog Reference ....!')
          

    def Azcomp_tests(self, chipid=1):
        #####################################CURR_3RD_STG_COMP
        rd3_current=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x00])
        sleep(2)
        self.PowerSupply.outp_OFF(3)
        self.PowerSupply.outp_ON(3)
        
        self.PowerSupply.setRange_Current(3,10**(-6))
        log.info(f'3rd_stg_curr_azcomp {self.PowerSupply.getCurrent(3)}')
        rd3_current.append(float(self.PowerSupply.getCurrent(3)))
        print("3rd_stg_curr_azcomp:", rd3_current)

        #####################################CURR_2RD_STG_COMP
        rd2_current=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x01])
        sleep(2)
        self.PowerSupply.setRange_Current(3,10**(-6))
        log.info(f'2rd_stg_curr_azcomp {self.PowerSupply.getCurrent(3)}')
        rd2_current.append(float(self.PowerSupply.getCurrent(3)))
        print("2rd_stg_curr_azcomp:", rd2_current)

        #####################################CURR_1RD_STG_COMP
        rd1_current=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x02])
        sleep(2)
        self.PowerSupply.setRange_Current(3,10**(-6))
        log.info(f'1rd_stg_curr_azcomp {self.PowerSupply.getCurrent(3)}')
        rd1_current.append(float(self.PowerSupply.getCurrent(3)))
        print("1rd_stg_curr_azcomp:", rd1_current)

        input('Change DMM')

        #####################################GND
        gnd_V=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x03])
        sleep(2)
        log.info(f'GND_V {self.Multimeter34410A.meas_V()}')
        gnd_V.append(float(self.Multimeter34410A.meas_V()))
        print("GND_V:", gnd_V)

        #####################################VCM
        VCM=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x0F])
        sleep(2)
        log.info(f'VCM {self.Multimeter34410A.meas_V()}')
        VCM.append(float(self.Multimeter34410A.meas_V()))
        print("VCM:", VCM)

        input('Measure differential voltage on OUTP and OUTN with the DMM')

        OUTN_EXT_PRT=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x0B])
        sleep(2)
        self.PowerSupply.emulMode_2Q(3)
        self.PowerSupply.setVoltage(3,2)
        self.PowerSupply.setVoltage(1,2)
        log.info(f'OUTN_EXT_PRT {self.Multimeter34410A.meas_V()}')
        OUTN_EXT_PRT.append(float(self.Multimeter34410A.meas_V()))
        print("OUTN_EXT_PRT:", OUTN_EXT_PRT)

        OUTP_EXT_PRT=[]
        self.mcp.mcpWrite(SlaveAddress=0x6c, data=[0x1A,0x0C])
        sleep(2)
        self.PowerSupply.emulMode_2Q(3)
        self.PowerSupply.setVoltage(3,2)
        self.PowerSupply.setVoltage(1,2)
        log.info(f'OUTP_EXT_PRT {self.Multimeter34410A.meas_V()}')
        OUTP_EXT_PRT.append(float(self.Multimeter34410A.meas_V()))
        print("OUTP_EXT_PRT:", OUTP_EXT_PRT)

        os.makedirs('measurements',exist_ok=True)
        with open('measurements/AzComp.json', 'r') as file :
            data = json.load(file)
            if str(chipid) not in data:
                data.update({
                    chipid:{
                        'curr_3rd_stg':rd3_current[-1],
                        'curr_2rd_stg':rd2_current[-1],
                        'curr_1rd_stg':rd1_current[-1],
                        'GND':gnd_V[-1],
                        'VCM':VCM[-1],
                        'OUTN_EXT_PRT':OUTN_EXT_PRT[-1],
                        'OUTP_EXT_PRT':OUTP_EXT_PRT[-1]
                    }
                })
                with open('measurements/AzComp.json', 'w') as file :
                    json.dump(data,file)
            else:
                log.warning(f'chip id {chipid} data already exits')


if __name__ == '__main__':
    AzComp(chipid=1)