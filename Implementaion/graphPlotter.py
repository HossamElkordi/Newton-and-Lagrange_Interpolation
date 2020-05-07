from time import time
from tkinter import ttk

from matplotlib import style
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

style.use('ggplot')


class graphPlotter():

    def __init__(self, frame, expression, xes, yes, solver):
        self.frame = frame
        self.fig = Figure(figsize=(5, 5), dpi=80)
        self.plt = self.fig.add_subplot(1, 1, 1)

        self.solver = solver
        self.xes = xes
        self.yes = yes
        self.expression = expression

        self.fx = np.arange(min(self.xes), max(self.xes) + 0.2, 0.2)
        self.fy = np.array([self.solver.evaluate(self.expression, num) for num in self.fx])
        self.plt.plot(self.fx, self.fy, color='r', label='y(x)')
        self.plt.scatter(self.xes, self.yes, color='b', label='Dataset')
        self.plt.axhline(y=0, color='k', label='X-Axis')
        self.plt.axvline(x=0, color='k', label='Y-Axis')
        self.plt.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, expand=True)
        self.canvas.get_tk_widget().pack(side=tk.TOP, expand=True)