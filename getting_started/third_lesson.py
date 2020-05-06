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

		# Creating a label and setting an alignment
		label = QLabel("thats a label")
		label.setAlignment(Qt.AlignCenter)
		self.setCentralWidget(label)

		# Creating a toolbar
		toolbar = QToolBar("My main toolbar")
		self.addToolBar(toolbar)

		# Creating a button
		button_action = QAction(QIcon("palette.png"),"Your button", self)
		button_action.setStatusTip("This is your button")
		button_action.triggered.connect(self.onMyToolBarButtonClick)
		# To change between true and false
		button_action.setCheckable(True)
		toolbar.addAction(button_action)

		# Add a separator between the buttons
		toolbar.addSeparator()

		# Add more buttons
		button_action2 = QAction(QIcon("palette--plus.png"),"Your button2", self)
		button_action2.setStatusTip("This is your button")
		button_action2.triggered.connect(self.onMyToolBarButtonClick)
		# To change between true and false
		button_action2.setCheckable(True)
		toolbar.addAction(button_action2)

		toolbar.addSeparator()

		toolbar.addWidget(QLabel("Hello"))
		
		toolbar.addSeparator()

		toolbar.addWidget(QCheckBox())

		# Add status bar when rover the button (tip)
		self.setStatusBar(QStatusBar(self))

	def onMyToolBarButtonClick(self, s):
		print('click', s)

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