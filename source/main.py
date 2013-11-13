import sys
import serial
import serial.tools.list_ports
from PyQt4.QtGui import QApplication, QMainWindow, QTextCursor
from PyQt4.QtCore import QThread, QObject, pyqtSignal, Qt
from ui_mainWindow import Ui_MainWindow

baudRates = ['300', '1200', '2400', '4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200', '230400']

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ser = None
        self.receiveData = ReadPort()
        self.sendData = WritePort()
        self.ui = Ui_MainWindow()
        self.setupUi()

    def closeEvent(self, event):
        self.closePort()
        QMainWindow.closeEvent(self, event)

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.comboBox_Bandrate.addItems(baudRates)
        self.refreshComboBoxPortName()
        # TODO QObject.connect(self.ui.comboBox_PortName, SIGNAL("activated()"), self.refreshComboBoxPortName)
        self.ui.pushButton_OpenPort.clicked.connect(self.openPort)
        self.ui.pushButton_ClosePort.clicked.connect(self.closePort)
        self.ui.pushButton_SendCmd.clicked.connect(self.sendCommand)

        self.receiveData.newData.connect(self.printComPortData)
        self.receiveData.error.connect(self.printError)
        self.sendData.error.connect(self.printError)

    def refreshComboBoxPortName(self):
        self.ui.comboBox_PortName.clear()
        self.ui.comboBox_PortName.addItems(self.getPortName())

    def getPortName(self):
        portNames = []
        try:
            for port in serial.tools.list_ports.comports():
                portNames.append(port[0])
        except:
            portNames.append('null')
            self.printError("Failed to scan port!")
        return portNames

    def getPortConfig(self):
        " Get port setting from ui "
        return self.ui.comboBox_PortName.currentText()

    def getBandRateConfig(self):
        " Get baudrate setting from ui "
        return self.ui.comboBox_Bandrate.currentText()

    def printComPortData(self, text):
        self.ui.plainTextEdit_txtDisplay.moveCursor(QTextCursor.End)
        self.ui.plainTextEdit_txtDisplay.insertPlainText(text)
        self.ui.plainTextEdit_txtDisplay.moveCursor(QTextCursor.End)
 
    def printInfo(self, text):
        " Print information to ui "
        self.ui.plainTextEdit_txtDisplay.appendPlainText(text)
        self.ui.plainTextEdit_txtDisplay.moveCursor(QTextCursor.End)

    def printError(self, text):
        " Print error to ui "
        self.ui.plainTextEdit_txtDisplay.appendPlainText(text)
        self.ui.plainTextEdit_txtDisplay.moveCursor(QTextCursor.End)

    def printCommand(self, text):
        " Print error to ui "
        self.ui.plainTextEdit_txtDisplay.appendPlainText("> " + text + "\n")
        self.ui.plainTextEdit_txtDisplay.moveCursor(QTextCursor.End)

    def sendCommand(self):
        " Send command string to com port "
        self.ui.comboBox_CommandInput.lineEdit().returnPressed.emit()
        cmd = self.ui.comboBox_CommandInput.currentText()
        cmd = cmd.replace("\\x16", "\x16", cs=Qt.CaseInsensitive)
        cmd = cmd.replace("\\x0d", "\x0d", cs=Qt.CaseInsensitive)
        self.printCommand(cmd)
        self.sendData.start(self.ser, cmd)
        #self.ui.cmdLineEdit.clear()

    def openPort(self):
        " Open serial port "
        self.closePort()
        try:
            self.printInfo("Connecting to %s with %s baud rate." % (self.getPortConfig(), self.getBandRateConfig()))
            self.ser = serial.Serial(str(self.getPortConfig()), int(self.getBandRateConfig()))
            self.receiveData.start(self.ser)
            self.printInfo("->>- Connected successfully.")
        except:
            self.ser = None
            self.printError("Failed to connect!")

    def closePort(self):
        " Close serial port "
        if self.receiveData.isRunning():
            self.receiveData.terminate()
        if self.sendData.isRunning():
            self.sendData.terminate()
        if self.ser == None: return
        try:
            if self.ser.isOpen:
                self.ser.close()
                self.printInfo("-<>- Disconnected successfully.")
        except:
            self.printError("Failed to disconnect!")
        self.ser = None


class ReadPort(QThread):
    newData = pyqtSignal(str)
    error = pyqtSignal(str)

    def start(self, ser, priority = QThread.InheritPriority):
        " Start receiving data from port "
        self.ser = ser
        QThread.start(self, priority)

    def run(self):
        " Reading data from port "
        while True:
            try:
                data = self.ser.read(1)
                n = self.ser.inWaiting()
                if n:
                    data = data + self.ser.read(n)
                self.newData.emit(data)
            except:
                errMsg = "Reader thread is terminated unexpectedly."
                self.error.emit(errMsg)
                break

    #def terminate(self):
    #    " Terminate data receiving "


class WritePort(QThread):
    error = pyqtSignal(str)

    def start(self, ser, cmd = "", priority = QThread.InheritPriority):
        " Start sending data to port "
        self.ser = ser
        self.cmd = cmd
        QThread.start(self, priority)

    def run(self):
        " Sending data to port "
        try:
            self.ser.write(str(self.cmd))
        except:
            errMsg = "Writer thread is terminated unexpectedly."
            self.error.emit(errMsg)

    def terminate(self):
        " Terminate sending data "
        self.wait()
        QThread.terminate(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
