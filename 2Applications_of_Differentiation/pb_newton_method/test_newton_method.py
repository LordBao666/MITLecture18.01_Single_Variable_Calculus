"""
@Author  : Lord_Bao
@Date    : 2021/4/18

"""

import math

"""
这个Part的复习课一个题是 
求解 
2cosx = 3x 的根，根据牛顿法思想，我们转换为
f(x) = 2cosx - 3x =0 时的根

f‘(x) = -2sinx - 3 
f''(x) = -2cosx 

满足  f’(x)的绝对值不太小  f‘’（x)  的绝对值不太大的条件。 

"""


def fx(x):
    return 2 * math.cos(x) - 3 * x


def fprime(x):
    return -2 * math.sin(x) - 3


def newton_method(x0, func, fprime_func, epsilon=1e-5, to_print=False):
    """
    xn+1 = xn  - f(xn)/fprime(xn)

    当xn  趋近于  真实跟 x时，必然有  |f(xn)|  < epsilon。
    这只是一个必要条件。

    由于牛顿迭代法的内在原理并不清楚，所以迭代终止条件可能不太正确。
    也就是最终的根可能并不是正确的。
    """
    guess_count = 1  # 代表估计次数
    if to_print:
        print("第{}次".format(guess_count), "x={}".format(x0), "fx={}".format(func(x0)))
    if abs(func(x0)) < epsilon:
        return x0

    xn_0 = x0
    xn_1 = xn_0 - func(xn_0) / fprime_func(xn_0)

    while True:
        guess_count += 1
        if to_print:
            print("第{}次".format(guess_count), "x={}".format(xn_1), "fx={}".format(func(xn_1)))
        if abs(func(xn_1)) < epsilon:
            return xn_1
        xn_0 = xn_1
        xn_1 = xn_0 - func(xn_0) / fprime_func(xn_0)


#  0 为 实际根的附近点
root = newton_method(0, fx, fprime, to_print=True)
print("根为{}".format(root))

root = newton_method(15, fx, fprime, to_print=True)
print("根为{}".format(root))