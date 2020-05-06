from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys 
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [50,35,44,22,38,32,27,38,32,44]


        # Plot data x, y values
        '''
        Colour                  Letter code
        blue                        b
        green                       g
        red                         r
        cyan (bright blue-green)    c
        magenta (bright pink)       m
        yellow                      y
        black                       k
        white                       w 
        '''
        #self.graphWidget.setBackground('#bbccaa')
        #self.graphWidget.setBackground('w')
        
        self.graphWidget.setBackground('w')

        #pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)
        pen = pg.mkPen(color=(255, 0, 0), width=5)
                
        self.graphWidget.plot(hour, temperature_1, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))
        self.graphWidget.setTitle('Your Title Here')
        self.graphWidget.setLabel('left', 'Temperature (°C)', color='red', size=30)
        self.graphWidget.setLabel('bottom', 'Hour (H)', color='red', size=30)

        self.graphWidget.addLegend()

        self.graphWidget.showGrid(x=True, y=True)

        # Setting axis limit
        #self.graphWidget.setXRange(5, 20, padding=0)
        #self.graphWidget.setYRange(30, 40, padding=0)

        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')
        '''
        Variable    Marker Type     
        o   Circular    
        s   Square  
        t   Triangular  
        d   Diamond     
        +   Cross 
        '''

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()