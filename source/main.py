import sys
#from PyQt4.QtGui import QApplication
#from window import Window
#from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from ui_realtimeplot import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())