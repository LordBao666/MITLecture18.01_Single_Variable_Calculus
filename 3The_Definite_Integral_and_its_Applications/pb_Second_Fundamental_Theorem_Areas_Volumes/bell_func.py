"""
@Author  : Lord_Bao
@Date    : 2021/4/28

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
    res = (gap * y_array).sum()
    return res


def bell_func(x):
    return math.e ** (-(x ** 2))


real_ans = (math.pi ** (1 / 2)) / 2
real_ans = round(real_ans, 5)
lower_bound = 0
upper_bound = 100
ans = riemann_sum(bell_func, lower_bound, upper_bound, size=100000)
ans = round(ans, 5)
print("x={}".format(upper_bound), "ans={}".format(ans), "real ans={}".format(real_ans))
