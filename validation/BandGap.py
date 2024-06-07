from logger import log 
from IvmDriver.mcp2221 import MCP2221
import time 
class BandGap:

    def __init__(self) -> None:
        self.mcp = MCP2221()
        self.slaveAddress = 0x6C
        startup_instructions=[
        [0xFE,0x00],
        [0x00,0x0F],
        [0xFE,0x01],
        [0x2F,0xAA],
        [0x2F,0xBB],
        ]
        # 1,B0,0;0;0
        # 1,B0,8;7;4
        
        analog_test = [
        [0xFE,0x01],
        [0x0F,0x88],
        [0x10,0x08],
        [0x19,0x81],
        [0x1A,0x01],
        [0xB0,0x01],
        ]

        for instruction in startup_instructions:
            self.mcp.mcpWrite(SlaveAddress=self.slaveAddress,data=instruction)
        input('Remove Reset GPIO :>')
        for instruction in analog_test:
            self.mcp.mcpWrite(SlaveAddress=self.slaveAddress,data=instruction)
        
        for i in range(16):
            val = (0x1 | (i<<4))
            print(hex(val))
            self.mcp.mcpWrite(SlaveAddress=self.slaveAddress,data=[0xB0,val])
            time.sleep(0.2)


if __name__ == '__main__':
    bandGap = BandGap()
