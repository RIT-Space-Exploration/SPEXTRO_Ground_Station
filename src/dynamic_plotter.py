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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets


class DynamicPlotter(FigureCanvas):

    def __init__(self, title, num_samples, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

    #Not sure where the format variable is used here
    def add_line(self, name, x_data, y_data, format):
        line = Line2D(x_data, y_data)
        ax.add_line(line)
        ax.set_xlim(min(x), max(x))
        ax.set_ylim(min(y), max(y))
        ax.plot()
        lines[name] = line

    def add_data(self, name, x_data, y_data):
        line = lines[name]

        if len(line.get_xdata) < num_samples:
            line.set_xdata(numpy.append(line.get_xdata(), x_data))
            line.set_ydata(numpy.append(line.get_ydata(), y_data))
        else:
            # sets each data to the latest num_samples-1 points of data plus the new point
            line.set_xdata(numpy.append(line.get_xdata()[len(line.get_xdata)-num_samples+1:], x_data))
            line.set_ydata(numpy.append(line.get_ydata()[len(line.get_ydata)-num_samples+1:], y_data))

        lines[name] = line
