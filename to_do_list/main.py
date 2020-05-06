import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

tick = QtGui.QImage('tick-button.png')


class TodoModel(QtCore.QAbstractListModel):
	def __init__(self, *args, todos=None, **kwargs):
		super(TodoModel, self).__init__(*args, **kwargs)
		self.todos = todos or []

	def data(self, index, role):
		if role == Qt.DisplayRole:
			_, text = self.todos[index.row()]

			return text

		if role == Qt.DecorationRole:
			status, _ = self.todos[index.row()]
			if status:
				return tick

	def rowCount(self, index):
		return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		#self.model = TodoModel(todos=[(False, 'my first todo')])
		self.model = TodoModel()
		
		# Loading data
		self.load()

		self.todoView.setModel(self.model)

		# Connect the button
		self.addButton.pressed.connect(self.add)
		self.deleteButton.pressed.connect(self.delete)
		self.completeButton.pressed.connect(self.complete)

	def add(self):
		"""
		Add an item to our todo list getting the text from
		Qlineedit and then ckearing it
		"""
		text = self.todoEdit.text()
		if text:
			# Access the list via model
			self.model.todos.append((False, text))
			# Trigger refresh
			self.model.layoutChanged.emit()
			# Empty the list
			self.todoEdit.setText("")
			self.save()

	def delete(self):
		indexes = self.todoView.selectedIndexes()
		if indexes:
			# Indexes is a list of a single item in single-select mode
			index = indexes[0]
			# Remoce the item and refresh
			del self.model.todos[index.row()]
			self.model.layoutChanged.emit()
			# Clear the selection
			self.todoView.clearSelection()

	def complete(self):
		indexes = self.todoView.selectedIndexes()
		if indexes:
			index = indexes[0]
			row = index.row()
			status, text = self.model.todos[row]
			self.model.todos[row] = (True, text)

			# Data changed takes top left and bottom right
			# wichh are equal for a single selection
			self.model.dataChanged.emit(index, index)
			# Clear the selection (as it no longer valid)
			self.todoView.clearSelection()
			self.save()

	def load(self):
		try:
			with open('data.json', 'r') as f:
				self.model.todos = json.load(f)

		except Exception:
			pass

	def save(self):
		with open('data.json', 'w') as f:
			data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()