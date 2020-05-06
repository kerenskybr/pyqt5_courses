import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
# To contert the ui file to python
# pyuic5 mainwindow.ui -o MainWindow.py

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()