import sys
import serial
import serial.tools.list_ports
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QThread, QObject # TODO: SIGNAL
from ui_mainWindow import Ui_MainWindow

baudRates = ['300', '1200', '2400', '4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200', '230400']

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.comboBox_Bandrate.addItems(baudRates)
        self.refreshComboBoxPortName()
        # TODO
        #QObject.connect(self.ui.comboBox_PortName, SIGNAL("activated()"), self.refreshComboBoxPortName)

    def refreshComboBoxPortName(self):
        self.ui.comboBox_PortName.clear()
        self.ui.comboBox_PortName.addItems(self.getPortName())

    def getPortName(self):
        portNames = []
        for port in serial.tools.list_ports.comports():
            portNames.append(port[0])
        return portNames

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
