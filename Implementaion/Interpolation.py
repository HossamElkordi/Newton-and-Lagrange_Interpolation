import numpy
from math import *
class Interpolation:
    def __init__(self, expression):
        self.expression = expression

    def f(self, x):
        return self.evaluate(x)

    def evaluate(self, x):
        return eval(self.expression)

    def newton_coeff(self, function, xes):
        yes = numpy.empty(0)
        list.sort(xes)
        xes = numpy.array(xes)
        l = len(xes)
        for i in range(l):
            yes = numpy.append(yes, round(self.evaluate(i)))
            continue
        for k in range(1, l):
            yes[k:l] = (yes[k:l] - yes[k - 1])/(xes[k:l] - xes[k - 1])
        return yes
#https://stackoverflow.com/questions/14823891/newton-s-interpolating-polynomial-python
#with 2 votes