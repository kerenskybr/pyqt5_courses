from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

app = QtWidgets.QApplication([])
volume = PowerBar(["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f", "#9e0142"])
volume.setBarPadding(2)
volume.setBarPadding(2)
volume.setBarSolidPercent(0.9)
volume.setBackgroundColor('gray')
volume.show()
app.exec_()