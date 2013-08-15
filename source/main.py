import sys
#from PyQt4.QtGui import QApplication
#from window import Window
#from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from PyQt4 import QtCore
from ui_realtimeplot import Ui_MainWindow
## import serial


## class SerialPort(serial.Serial):
##     """Serial port init, config, data receive and data sending."""

##     def __init__(self):
##         try:
##             self.ser = serial.Serial(
##                 port='com1',
##                 baudrate=115200,
##                 bytesize=serial.EIGHTBITS,
##                 parity=serial.PARITY_NONE,
##                 stopbits=serial.STOPBITS_ONE,
##                 timeout=0.1,
##                 xonxoff=0,
##                 rtscts=0,
##                 interCharTimeout=None
##             )
##         except serial.serialutil.SerialException:
##             #no serial connection
##             self.ser = None
##         else:
##             #Thread(target=receiving, args=(self.ser,)).start()
##             pass

##     def Connect(self):
##         pass

##     def Disconnect(self):
##         pass


## class DataReader(QtCore.QThread):
##     "loop and copy serial->console"
##     def __init__(self, port_src=None):
##         #QtCore.QThread.__init__(self)
##         super(DataReader, self).__init__()
##         self.port_src = port_src

##     def run(self):
##         while 1:
##             ser_data_queue = self.port_src.read(1)
##             window.plainTextEdit.appendPlainText('s')


## class DataWriter(QtCore.QThread):
##     ""
##     def __init__(self, port_tar=None):
##         #QtCore.QThread.__init__(self)
##         super(DataReader, self).__init__()
##         self.port_tar = port_tar

##     def run(self):
##         for i in range(50):
##             print 'W%r' % (i)


## def data_dispatch():
##     "send the data to terminal window or plot panel"
##     pass


## def plot():
##     "plot the data"
##     pass


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.actionOpen_port.triggered.connect(self.openPort)
        self.actionClose_port.triggered.connect(self.closePort)

    def openPort(self):
        " open port ttt"

        print 'Open port'

    def closePort(self):
        print 'Close port'


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
