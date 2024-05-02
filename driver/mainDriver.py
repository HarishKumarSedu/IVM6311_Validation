from PyQt5 import QtWidgets,QtGui,QtCore,uic
import sys 
from matrix import Matrix
from driver import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.matrix = Matrix()
        self.setupUi(self)
        
        self.pushButton_2.clicked.connect(self.addMatrix)

        self.matrixLayout = {}
        self.matrixIndex = 0
    def addMatrix(self):
        
        self.matrixLayout.update({
            self.matrixIndex : Matrix(deviceAddress=0x20+self.matrixIndex*4)
        })
        self.scrollAreaWidgetContentsverticalLayout.addWidget(list(self.matrixLayout.values())[-1])
        self.matrixIndex += 1 
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())