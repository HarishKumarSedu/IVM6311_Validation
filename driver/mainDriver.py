from PyQt5 import QtWidgets,QtGui,QtCore,uic
import sys 
from matrix import Matrix
from driver import Ui_MainWindow
import json 



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.matrix = Matrix()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.addMatrixPushButton.clicked.connect(self.addMatrix)

        self.lockConfigPushButton.clicked.connect(self.lockConfig)
        self.generateConfigPushButton.clicked.connect(self.generateConfig)
        
        self.matrixLayout = {}
        self.matrixIndex = 0
        with open(f'styles/scrollAreaFrame.qss', 'r') as file:
            self.scrollArea.setStyleSheet(file.read())
            
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # handle the left-button press in here
             self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x()+delta.x(),self.y() + delta.y())
        self.oldPosition = event.globalPos()
        
    def addMatrix(self):
        
        self.matrixLayout.update({
            self.matrixIndex : Matrix(deviceAddress=0x20+self.matrixIndex*4)
        })
        self.scrollAreaContentsverticalLayout.addWidget(list(self.matrixLayout.values())[-1])
        self.matrixIndex += 1 
        
    def lockConfig(self):
        if checked := self.lockConfigPushButton.isChecked() :
            for lineEdit  in list(self.matrixLayout.values()):
                lineEdit.locked = False
                lineEdit.freezeLineEdit()
                
        else:
            for lineEdit  in list(self.matrixLayout.values()):
                lineEdit.locked = True
                lineEdit.freezeLineEdit()
            
    
    def generateConfig(self):
        if not self.lockConfigPushButton.isChecked() :
            SignalConfig = {}
            for index,matrix  in self.matrixLayout.items():
                SignalConfig.update(
                    {
                        index:matrix.getConfig()
                    }
                )
            with open(f'signals/dummysignalconfig.json','w') as file :
                json.dump(SignalConfig,file)
                
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    with open('styles/app.qss',"r") as appStyles :
        app.setStyleSheet(appStyles.read())
    window.show()
    sys.exit(app.exec())