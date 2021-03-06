import numpy


class Interpolation:
    def __init__(self):
        pass

    def evaluate(self, exp, x):
        return eval(exp)

    def newton_coeff(self, xes, yes):
        xes = numpy.copy(xes)
        yes = numpy.copy(yes)
        l = len(xes)
        for k in range(1, l):
            yes[k:l] = (yes[k:l] - yes[k - 1]) / (xes[k:l] - xes[k - 1])
        return yes

    def Newton(self, xes, yes, X):
        self.bubbleSortxy(xes, yes)
        coefficient = self.newton_coeff(xes, yes)
        degree = len(xes) - 1
        answer = []
        string = ''
        rounded = ''
        for i in range(0, len(coefficient)):
            if i == 0:
                string = str(coefficient[i])
                rounded = str(round(coefficient[i], 5))
            elif coefficient[i] < 0:
                string = string+str(coefficient[i])+'*'
                rounded = rounded + str(round(coefficient[i], 5)) + '*'
            else:
                string = string+'+'+str(coefficient[i])+'*'
                rounded = rounded+'+'+str(round(coefficient[i], 5)) + '*'
            for j in range(0, i):
                if xes[j] < 0:
                    string = string+'(x+'+str(abs(xes[j]))+')'
                    rounded = rounded + '(x+' + str(round(abs(xes[j]), 5)) + ')'
                else:
                    string = string + '(x-' + str(xes[j]) + ')'
                    rounded = rounded + '(x-' + str(round(xes[j], 5)) + ')'
                if j < i-1:
                    string = string + '*'
                    rounded = rounded + '*'
        for x in X:
            y = coefficient[degree]
            for i in range(1, degree + 1):
                y = coefficient[degree - i] + (x - xes[degree - i]) * y
            answer.append(y)
        return [answer, string, rounded]


    def bubbleSortxy(self, arrx, arry):
        n = len(arrx)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arrx[j] > arrx[j + 1]:
                    arrx[j], arrx[j + 1] = arrx[j + 1], arrx[j]
                    arry[j], arry[j + 1] = arry[j + 1], arry[j]

    def laGrange(self, xes, yes, query):
        self.bubbleSortxy(xes, yes)
        helper = self.laGrangeHelper(xes, yes)
        op = helper[0]
        other_yes = []
        for i in range(len(query)):
            other_yes.append(self.evaluate(op, query[i]))
        return [other_yes, op, helper[1]]


    def laGrangeHelper(self, xes, yes):
        rounded = ''
        op = "("
        n = len(xes)
        for i in range(n):
            op = op + "(("
            rounded = rounded + "(("
            for j in range(n):
                if j == i:
                    continue
                op = op + "("
                rounded = rounded + "("
                op = op + "(x-" + str(xes[j]) + ")/(" + str(xes[i] - xes[j]) + "))*"
                rounded = rounded + "(x-" + str(round(xes[j], 5)) + ")/(" + str(round(xes[i] - xes[j], 5)) + "))*"
            op = op[:-1]
            rounded = rounded[:-1]
            op = op + ")*" + str(yes[i]) + ")+"
            rounded = rounded + ")*" + str(round(yes[i], 5)) + ")+"
        op = op[:-1]
        rounded = rounded[:-1]
        op = op + ")"
        rounded = rounded + ")"
        return [op, rounded]