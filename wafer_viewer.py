# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:55:41 2020

@author: wtjang
"""



import pandas as pd 
test = pd.DataFrame(index=range(0,301), columns=range(0,301))     # 빈데이터 프레임

for i in range(0,301):
    for j in range(0,301):
        if ((150-i)**2 + (150-j)**2) < 150**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0




import pandas as pd 
test = pd.DataFrame(index=range(0,101), columns=range(0,101))     # 빈데이터 프레임

for i in range(0,101):
    for j in range(0,101):
        if ((50-i)**2 + (50-j)**2) < 50**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0



import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
test[test == 0] = np.nan
plt.figure(1)
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar()    

#fig1 = plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')

from PyQt5.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

#경로 주소 삽입
# The loadUiType function requires a single argument, the name of a Designer UI file
Ui_MainWindow, QMainWindow = loadUiType(r'C:\Users\wtjang\.spyder-py3\window.ui')

import numpy as np
from PyQt5 import QtWidgets 

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas) #mplvl
        self.canvas.draw()
 
if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
# error  name 'QtWidgets' is not defined  -> QtGui.QApplication([" "]) ->  QtWidgets.QApplication([" "]) 으로 변경
    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111) 
    ax1f1.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
 
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())