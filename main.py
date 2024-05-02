from driver.signalRoot import SignalRoot
from driver.mcp2317 import MCP2317
from ast import literal_eval
from time import sleep
from __init__ import log

if __name__ == '__main__':
    signalRoot = SignalRoot()
    signalRoot.signalPathMapping()
    signal = signalRoot.signalConfig(Source= {'High': 'BE+', 'Low': 'Batn'}, Destination= {'High': 'multip', 'Low': 'multin'}, Signalroot_file='driver/signals/signalroot_matrix.json')
    # signal = literal_eval(signal)
    print(type(signal))
    # mcp =MCP2317(DeviceAddr=literal_eval(signal.get('deviceAddr')))
    # mcp.Switch(row=signal.get('relay').get('row'), col=signal.get('relay').get('col'), Enable=True)
    
    
    