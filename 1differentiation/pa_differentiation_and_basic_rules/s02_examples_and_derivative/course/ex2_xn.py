"""
@Author  : Lord_Bao
@Date    : 2021/4/8

"""
import pylab
import numpy as np

"""
自定义求导数的函数get_derivative

本题求xn的导数，我们假定x=3
"""


def get_derivative(fx, x0, dx=1e-5, precision=4):
    """
    :param fx: 单变量函数fx,
    :param x0: 需要求导的x0
    :param dx: delta x ,刻画无穷小量,默认 1e-5
    :param precision: 默认精度为4，比如求导即为为   0.12432  那么默认返回 0.1243
    :return:
    """
    denominator = dx
    nominator = fx(x0 + dx) - fx(x0)
    return round(nominator / denominator, precision)


def xn(x, n):
    return x ** n


# 函数
x = np.arange(-2, 2, 0.01)
y = [xn(elt, 3) for elt in x]

# n=3时的xn函数
xn_3 = lambda elt: xn(elt, 3)
# 导数
derivative_y = [get_derivative(xn_3, elt) for elt in x]

pylab.xlabel("x")
pylab.ylabel("f(x)")
pylab.plot(x, y, label="f(x)=x^3")
pylab.plot(x, derivative_y, label="f'(x)")
pylab.legend(loc="best")
pylab.show()
