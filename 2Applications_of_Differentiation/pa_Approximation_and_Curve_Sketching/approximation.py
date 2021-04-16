"""
@Author  : Lord_Bao
@Date    : 2021/4/16

"""
from scipy.misc import derivative
import math
import numpy as np
import pylab

"""
f(x) 的近似估计  
Bad Code  !!!!   scipy.misc import derivative 求高阶导时会出错，原因不明，比如sinx 的4阶导竟然求出来3位数
如果dx取得过小，就会出现这种情况.那么将dx取大一点不行吗？ 我认为这就是诡异的地方，求极限为什么还要把dx取大。


我原先基本思路是，取一个起始点 begin 然后设置gap,并产生若干数字 begin，begin+1gap,begin+2gap,begin+3gap

并使 x0 = begin + n* gap  ,near_x0 = x0 + gap。（n = 0,1 2,....n)

然后用 A(near_x0)  去估计 f(near_x0) ,A(near_x0)  =     关于x0  n次估计式 中 x 取 near_x0的值。

如果gap取得够小，那么应该高阶的估计式应更加贴近f(x)。

1.将估计式计算出来的值用于作图,然后观察不同次数的估计式的区别不太现实，因为gap很小的时候,细微差别难以观察
参看ex.png。

2.具体的做法应该是  求和（（Ti-Ti估计）/ Ti） i从1到n  /  n
  不知道pylab会不会根据y轴调尺度，如果可以的话，就可以看出来不同多项式的近似程度。如果不行的话，可以将
  上述的结果通通 乘以一个 共同的比较大的数 比如10000 。 那么可以观察出不同次数的差别了。
  
  
问题是现在n次求导的库我没找到。
scipy.misc import derivatie  在高阶上(比如n=3,4,5）的计算值是很差的。


暂时这样吧，弄了一个下午

"""

def polynomial_approximation(func, x0, near_x0, n=1, order=3):
    """
    :param func: 将被线性估计的单变量函数
    :param x0  x0
    :param near_x0  near_x0是x0附近的值.用A(near_x0) 预估 f(near_x0)
    :param n:n次估计 ，默认为1，即线性估计
    :param order : int, optional
        Number of points to use, must be odd. 我也不知道是什么意思。先满足要求再说。
    :return: 返回基于x0的  A(near_x0)
    """

    ret = 0.0
    for i in range(n + 1):
        # i次导 (注意order的数字必须至少为 求导次数 + 1,并且为奇数,默认为3
        ith_derivative = derivative(func, x0, dx=1e-5, n=i, order=order)
        # i阶层
        i_factorial = math.factorial(i)
        # i次 指数式
        i_power_term = (near_x0 - x0) ** i

        # 结果
        term = ith_derivative * i_power_term / i_factorial

        # 累加
        ret += term
    return ret


# 测试   ##
x0 = 0
near_x0 = 1
ret = polynomial_approximation(math.sin, x0, near_x0, n=5, order=9)
print(ret)
print(math.sin(near_x0))
# 测试   ##



