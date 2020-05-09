#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 15, 2020 05:32:31 PM +0200  platform: Windows NT

import time
import traceback

from Implementaion import Interpolation as inter
from Implementaion import graphPlotter as gp

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

from tkinter.filedialog import *


def set_Tk_var():
    global combo_box
    combo_box = tk.StringVar()
    global x_input
    x_input = tk.StringVar()
    global y_input
    y_input = tk.StringVar()
    global x_points
    x_points = tk.StringVar()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def interpolate(txt, gph):
    for widget in gph.winfo_children():
        widget.destroy()
    txt.delete("1.0", tk.END)
    method = combo_box.get().lower()
    try:
        x = string_to_list(x_input.get())
        y = string_to_list(y_input.get())
        xes = string_to_list(x_points.get())
        solver =inter.Interpolation()
        if len(x) != len(y):
            traceback.print_exc()
            txt.insert(tk.END, 'Wrong input format')
        if method == 'newton method':
            current = time.time() * 1000
            answer = solver.Newton(x, y, xes)
            s = print_newton(txt, xes, answer, current)
            current = time.time() * 1000
        elif method == 'lagrange method':
            current = time.time() * 1000
            answer = solver.laGrange(x, y, xes)
            s = print_lagrange(txt, xes, answer, current)
        txt.insert(tk.END, s)
        gp.graphPlotter(gph, answer[1], x, y, solver)

    except Exception:
        traceback.print_exc()
        txt.insert(tk.END, 'Wrong input format')
    sys.stdout.flush()


def string_to_list(string):
    i_prev = 0
    my_list = []
    test_list = ['.']
    for i in range(0, len(string)):
        if string[i] == ',':
            temp = string[i_prev: i]
            if [ele for ele in test_list if (ele in temp)]:
                my_list.append(float(temp))
                i += 1
            else:
                my_list.append(int(temp))
                i += 1
            i_prev = i
    temp = string[i_prev: (len(string))]
    if [ele for ele in test_list if (ele in temp)]:
        my_list.append(float(temp))
    else:
        my_list.append(int(temp))
    return my_list


def print_newton(console, xes, answer, current):
    y_list = answer[0]
    s = ''
    s += 'y(x): {}\n'.format(answer[2])
    s += 'Execution time: {} milliseconds\n'.format(time.time() * 1000 - current)
    s += 'Points calculated with y(x): ({}, {})\n'.format(xes[0], round(y_list[0], 5))
    if len(xes) > 1:
        for i in range(1, len(xes)):
            s += '\t\t\t     ({}, {})\n'.format(xes[i], round(y_list[i], 5))
    return s


def print_lagrange(console, xes, answer, current):
    y_list = answer[0]
    s = ''
    s += 'y(x): {}\n'.format(answer[2])
    s += 'Execution time: {} milliseconds\n'.format(time.time() * 1000 - current)
    s += 'Points calculated with y(x): ({}, {})\n'.format(xes[0], round(y_list[0], 5))
    if len(xes) > 1:
        for i in range(1, len(xes)):
            s += '\t\t\t     ({}, {})\n'.format(xes[i], round(y_list[i], 5))
    return s

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import InterpolationGui

    InterpolationGui.vp_start_gui()