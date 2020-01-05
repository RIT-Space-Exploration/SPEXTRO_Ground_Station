"""
File: dynamic_plotter.py
Org: RIT Space Exploration
Desc:
    Class which contains and provides functionality for dynamically
    plotting data on arrival.

add_line(name, x_data, y_data, format): This method should use .plot() provided by the ax
variable:matplotlib.axes.Axes to add and return the new line. This new line should be added into the
lines:dictstr:matplotlib.lines.Line2D with the name is the key and the newly created line object.

add_data(name, x_data, y_data): This method should update the data for the line with the key name. Data should be
appended to until the length of the data in the line equals num_samples. From then on, data at the front of the list
provided by calling get_data should be removed and new data added to the back of that list. The x_data and y_data
variables will be not included in a 'many' data structure thus having a sample size of one. So one old x and y data
point will be removed and one new x and y data point added.

"""
from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class DynamicPlotter(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.add_line('origin', [0], [0])

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def add_line(self):
        pass



class MyDynamicMplCanvas(DynamicPlotter):

    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        DynamicPlotter.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def add_line(self, name, x_data, y_data, format=None):
        lines[name] = plt.Line2D(x_data, y_data, format)

    def update_figure(self):
        x_data = [random.randint(0, 10)]
        y_data = [random.randint(0, 10)]
        self.axes.cla()
        self.add_data('origin', x_data, y_data)
        line = lines['origin']
        self.axes.plot(line.get_xydata())
        self.draw()

    def add_data(self, name, x_data, y_data):
        line = lines[name]

        line.set_data(line.get_xdata() + x_data, line.get_ydata() + y_data)

        lines[name] = line



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        #sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #l.addWidget(sc)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """balls"""
                                )


lines = {}

qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()
