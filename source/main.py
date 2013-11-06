import sys
import serial
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QThread
from ui_mainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)

    def openPort(self):
        " Open serial port "

    def closePort(self):
        " Close serial port "

class ReadPort(QThread):
    def start(self):
        " Start receiving data from port "

    def run(self):
        " Reading data from port "

    def terminate(self):
        " Terminate data receiving "

class WritePort(QThread):
    def start(self):
        " Start sending data to port "

    def run(self):
        " Sending data to port "

    def terminate(self):
        " Terminate sending data "

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
