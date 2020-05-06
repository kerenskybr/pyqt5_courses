import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import datetime
import numpy as np

class TableModel(QtCore.QAbstractTableModel):
    # __init__ is the constructor
    # This initialize the attributes of the class
    def __init__(self, data):
        # Super returns a temporary object thats allow to reference a 
        # parent class by the word super to avoid use super(parent)
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]
            return str(value)

            #return self._data[index.row()][index.column()]
            return value

    def rowCount(self, index):
        # the length of th eouter list
        return self._data.shape[0]

    def columnCount(self, index):
        # Takes the first sub-list and returns the length
        # the length (only works uf all rows are an equal length)
        return self._data.shape[1]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = np.array([
          [1, 9, 2],
          [1, 0, -1],
          [3, 5, 2],
          [3, 3, 2],
          [5, 8, 9],
        ])

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()