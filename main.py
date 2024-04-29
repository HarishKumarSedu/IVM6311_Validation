from driver.signalRoot import SignalRoot
from __init__ import log

if __name__ == '__main__':
    signalRoot = SignalRoot()
    signalRoot.signalPathMapping()
    print(signalRoot.signalConfig(Source={'High': 'BCLK', 'Low': 'SDI'}, Destination={'High': 'FSYN AP', 'Low': 'GND'}, Signalroot_file='driver/signals/signalroot_matrix.json'))