import numpy
from math import *


class Interpolation:
    def __init__(self, expression):
        self.expression = expression

    def newton_coeff(self, xes, yes):
        xes = numpy.copy(xes)
        yes = numpy.copy(yes)
        l = len(xes)
        for k in range(1, l):
            yes[k:l] = (yes[k:l] - yes[k - 1]) / (xes[k:l] - xes[k - 1])
        return yes

    def Newton(self, xes, yes, X):
        bubbleSortxy(xes, yes)
        coefficient = self.newton_coeff(xes, yes)
        degree = len(xes) - 1
        answer = []
        y = coefficient[degree]
        string = ''
        for i in range(0, len(coefficient)):
            if coefficient[i] < 0:
                string = string+str(coefficient[i])
            else:
                string = string+'+'+str(coefficient[i])
            for j in range(0, i):
                if xes[j] < 0:
                    string = string+'(x+'+str(abs(xes[j]))+')'
                else:
                    string = string + '(x-' + str(xes[j]) + ')'
#        string = str(y)
        for x in X:
            for i in range(1, degree + 1):
                y = coefficient[degree - i] + (x - xes[degree - i]) * y
#               string = '(' + str(coefficient[degree - i]) + '(x-' + str(xes[degree - i]) + ')' + string + ')'
            answer.append(y)
        return [answer, string]


# https://stackoverflow.com/questions/14823891/newton-s-interpolating-polynomial-python
# with 2 votes
def bubbleSortxy(arrx, arry):
    n = len(arrx)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arrx[j] > arrx[j + 1]:
                arrx[j], arrx[j + 1] = arrx[j + 1], arrx[j]
                arry[j], arry[j + 1] = arry[j + 1], arry[j]



def evaluate(exp, x):
    return eval(exp)

def laGrange(xes, yes, query):
    bubbleSortxy(xes, yes)
    op = laGrangeHelper(xes, yes)
    for i in range(len(query)):
        query[i] =  evaluate(op, query[i])
    return [op, query]


def laGrangeHelper(xes, yes):
    op = "("
    n = len(xes)
    for i in range(n):
        op = op + "(("
        for j in range(n):
            if j == i:
                continue
            op = op + "("
            op = op + "(x-" + str(xes[j]) + ")/(" + str(xes[i] - xes[j]) + "))*"
        op = op[:-1]
        op = op + ")*" + str(yes[i]) + ")+"
    op = op[:-1]
    op = op + ")"
    return op
