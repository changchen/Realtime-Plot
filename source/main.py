import sys
#from PyQt4.QtGui import QApplication
#from window import Window
#from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from ui_realtimeplot import Ui_MainWindow
import serial

class SerialPort:
    """Serial port init, config, data receive and data sending."""
    def __init__(self):
        try:
            self.ser = ser = serial.Serial(
                port='com57',
                baudrate=115200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )

        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
        else:
            #Thread(target=receiving, args=(self.ser,)).start()
            pass
            
    def SerDataReceive(self):
        pass


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())