"""
@Author  : Lord_Bao
@Date    : 2021/4/26

"""
import numpy as np
import math


def riemann_sum(func, lower_bound, upper_bound, size=1000):
    """
    :param func:将要进行黎曼和的单变量函数
    :param lower_bound: 积分下限
    :param upper_bound: 积分上限
    :param size: 取多少个区间，默认是1000
    :return: 黎曼和

    注意  根据f(xi) 的xi  是 第i个区间的任意一个数字即可.由于浮点是不精确的，
    所以选取每个区间的中间数字作为xi。而不是选取每个区间的首或尾作为xi.当然，个人感觉实际情况应该区别不大。

    """
    gap = (upper_bound - lower_bound) / size
    x_array = np.arange(lower_bound + gap / 2, upper_bound, gap)
    y_array = np.array([func(xi) for xi in x_array])
    # print("x =", x_array)
    # print("y =", y_array)
    res = (gap * y_array).sum()
    return res


def func1(x):
    return x ** 2


"""
测试riemann_sum
"""
# ans = riemann_sum(func1, 0, 2, size=2)
# print(ans)

"""
测试  y =x^2  在 [0,3]  的 riemann_sum
实际结果是  9
测试结果为  8.9999999775
"""
# ans = riemann_sum(func1, 0, 3, size=10000)
# print(ans)

"""
测试  y =sinx  在 [-pi,pi]  的 riemann_sum
实际结果是  0
测试结果为  1.1102230246251565e-16
"""
ans = riemann_sum(math.sin, -math.pi, math.pi, size=10000)
print(ans)
