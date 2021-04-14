"""
@Author  : Lord_Bao
@Date    : 2021/4/11

"""
import numpy as np
import pylab
import math

"""
find  e
函数  (1+1/n)^n   n趋于无穷
"""


def magic_func(n):
    return (1 + 1 / n) ** n


begin = 1
end = 100
gap = 1
x_vals = list(i for i in range(begin, end, gap))
y_vals = [magic_func(n) for n in x_vals]


pylab.plot(x_vals, y_vals, '.b', label="$y=(1+\\frac{1}{n})^n$")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.legend(loc="best")
pylab.show()
