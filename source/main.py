import sys
import serial
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtCore
from ui_mainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)

    def openPort(self):
        print 'Open port'

    def closePort(self):
        print 'Close port'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
