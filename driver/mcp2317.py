
from mcp2221 import MCP2221
from typing import Union
import warnings

class MCP2317:
    def __init__(self,DeviceAddr:hex) -> None:
        self.slaveAddress = DeviceAddr
        self.IODIRA = 0x00 # Bank GPIO congurations :  1 - InPut , 2 - Output ; default all Bank GPIOs are inputs 
        self.IODIRB = 0x01 
        self.GPIOA  = 0x12 # GPIO BANK output set 
        self.GPIOB  = 0x13 # GPIO BANK output set 
        
        self.mcp = MCP2221()
        
        self.AllOUTput = 0x00 # enable all the GPIO as output 
        self.AllINput = 0xFF  # configure all the gpios as inputs 
        self.ResetAllOUTput = 0x00 # open all the switches 
        self.SetAllOUTput = 0xFF   # close all the switches 
        
        self.configure()
        
    def configure(self,):
        self.mcp.Reset() # reset the mcp 
        self.mcp.GPIO_Init() # initialize the mcp gpios 
        self.mcp.GPIO_0_OutputMode() # set the gpio as output 
        self.mcp.GPIO_1_OutputMode()
        self.mcp.GPIO_2_OutputMode()
        self.mcp.GPIO_3_OutputMode()
        self.mcp.GPIO_2_Output(1) # Enable the GPIO output 
        self.mcp.GPIO_2_Output(1)
        self.mcp.GPIO_2_Output(1)
        self.mcp.GPIO_2_Output(1)
        self.mcp.mcpWrite(self.slaveAddress, [self.IODIRA, self.AllOUTput]) # configure all the bank A gpios are as outputs 
        self.mcp.mcpWrite(self.slaveAddress, [self.IODIRB, self.AllOUTput]) # configure all the bank B gpios are as outputs 
    
    def reset(self):
        self.mcp.mcpWrite(self.slaveAddress, [self.IODIRA, self.ResetAllOUTput]) # configure all the bank A gpios are as outputs 
        self.mcp.mcpWrite(self.slaveAddress, [self.IODIRB, self.ResetAllOUTput]) # configure all the bank B gpios are as outputs 

        # Hard reset the GPIO expanders 
        self.mcp.GPIO_2_Output(1) # Disable the GPIO output 
        self.mcp.GPIO_2_Output(1)
        self.mcp.GPIO_2_Output(1)
        self.mcp.GPIO_2_Output(1)
        
        # Reset the MCP
        self.mcp.Reset()
        
    
    
    def Switch(self,row=1, col =1, Enable = False):
        if  (0 > row <= 8) & (0 > col <= 8):
            # odd Row 
            if row % 2 :
                RegBank_addr = self.GPIOB
            else:
                RegBank_addr = self.GPIOA

            if Enable:
                data = self.mcp.mcpRead(self.slaveAddress, [RegBank_addr]) # Read the register bank data
                data = data | (1 << col-1)
                self.mcp.mcpWrite(self.slaveAddress, [RegBank_addr,data])
            else:
                data = self.mcp.mcpRead(self.slaveAddress, [RegBank_addr]) # Read the register bank data
                data = data & ~(1 << col-1)
                self.mcp.mcpWrite(self.slaveAddress, [RegBank_addr,data])
        else:
            warnings.warn(f'Signal Matrix Selection Outof  Context of the Matrix row :{row} ; col:{col}')
            
                    
                
                