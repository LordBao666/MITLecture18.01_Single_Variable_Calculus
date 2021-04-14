"""
@Author  : Lord_Bao
@Date    : 2021/4/11

"""

from scipy import optimize
import numpy as np
import pylab
import math

"""
求函数的根(这里尤其针对的是隐函数的根）


参考如下文章
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html#scipy.optimize.root

"""


def circle_func(y, x, r):
    """
     circle 函数
    严格来说，这不算严格函数，因为 x^2 + y^2 = r^2   因为x固定时，y有两个值。

    这里的参数顺序设置是根据
    scipy.optimize.root(fun, x0, args=(), method='hybr', jac=None, tol=None, callback=None, options=None)
    设置的。具体它的用法，参见learn_find_root.py

    """
    return x ** 2 + y ** 2 - r ** 2


def magic_func(y, x):
    """
    :param y:
    :param x:
    :return:

    函数  e^x+y  + xy - e =0
    特征，当其中一个确定为0时，另一个只能为1
    """
    return math.e ** (x + y) + x * y - math.e




"""
测试画圆  
"""
# ################################测试 x^2 + y^2 = r^2  采用求根方法##########################
# radius = 3
# gap = 0.01
# x_vals = np.arange(-radius, radius + gap, gap)
# y_vals = []
# for x in x_vals:
#     best_guess = 0.1  # 代表测试结果为0.1附近，这里作用其实是求非负根。
#     extra_argus = (x, radius)
#     ret = optimize.root(circle_func, np.array([best_guess]), extra_argus)
#     y_vals.append(ret.x[0])
#
# for x in x_vals:
#     best_guess = -0.1  # 代表测试结果为-0.1附近，这里作用其实是求非正根。
#     extra_argus = (x, radius)
#     ret = optimize.root(circle_func, np.array([best_guess]), extra_argus)
#     y_vals.append(ret.x[0])
#
# x_vals = np.concatenate((x_vals, x_vals))  # 传入一个元组，元组元素为将拼接的ndarry
# pylab.plot(x_vals, y_vals, '.b', label="$x^2 + y^2 ={}^2$".format(radius))
# pylab.xlabel("x")
# pylab.ylabel("y")
# # 坐标轴尺度相同
# pylab.axis("equal")
# pylab.legend(loc="best")
# pylab.show()

# ################################测试 x^2 + y^2 = r^2  采用求根方法##########################

"""
测试 e^(x+y)  + xy -e =0  特征，当其中一个确定为0时，另一个只能为1
"""
# ################################测试 e^(x+y)  + xy -e =0 ##########################

# # begin = - 3
# # end = 3
# # gap = 0.01
#
# # begin = - 1
# # end = 0
# # gap = 0.001
#
# begin = - 0.63
# end = -0.57
# gap = 0.0001
# x_vals = np.arange(begin, end + gap, gap)
# y_vals = []
# for x in x_vals:
#     best_guess = 0.1  #
#     extra_argus = (x,)
#     # method 默认是 hybr
#     ret = optimize.root(magic_func, np.array([best_guess]), extra_argus)
#     y_vals.append(ret.x[0])
#
#  注意不要采用默认的划线方式,容易造成困扰。
# pylab.plot(x_vals, y_vals, '.b', label="$e^{x+y} + xy - e =0$")
# pylab.title("x: begin:{}".format(begin) + ",end:{}".format(end))
# pylab.xlabel("x")
# pylab.ylabel("y")
# pylab.legend(loc="best")
# pylab.show()

# ################################测试 e^(x+y)  + xy -e =0 ##########################


