from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		# Signal: the connected function will be called whenever the window
		# title is changed. The new title will be passed to the function
		self.windowTitleChanged.connect(self.onWindowTitleChange)

		# Signal: The new title is discaded in the lambda func and the func
		# is called without params
		self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

		# The new title is passed to the function and replaces the default
		#  param
		self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

		# Extra data is passed within the lambda
		self.windowTitleChanged.connect(lambda x: self.my_custom_fn(25))

		# This sets the window title wich'll trigger all the above signals
		# sending the new title to the attached funcs or lambdas first param
		self.setWindowTitle("My App")

		label = QLabel("thats a label")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

	# Slot: This accepts a string e.g. the window title an prints it
	def onWindowTitleChange(self, s):
		print(s)

	#  Slot: this has a default param and can be called without a value
	def my_custom_fn(self, a="Hello", b=5):
		print(a, b)

	# It's intercept the signal event when you right click the window
	def contextMenuEvent(self, event):
		print("Context menu event!")
		super(MainWindow, self).contextMenuEvent(event)



app = QApplication(sys.argv)

window = MainWindow()
# Its like ptt.show()
window.show()

app.exec_()