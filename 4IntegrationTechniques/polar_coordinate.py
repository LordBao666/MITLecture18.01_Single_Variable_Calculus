"""
@Author  : Lord_Bao
@Date    : 2021/5/9

"""

import pylab
import numpy as np

"""
Demo1  玫瑰线
"""
# 假设参数a 为 2
a = 2
theta = np.arange(0, 2, 0.01) * np.pi
r = a * np.sin(2* theta)
# 下面的代码的意思是  如果 r小于0，那么theta将 加一个pi，并且将r做绝对值处理
# 之所以这样做的原因是 r在pylab中貌似不能为负值，所以做一定的数学处理
label = "$r={}\\sin2\\theta,\\theta\\in[0,2\\pi]$".format(a)
pylab.polar(theta + (r < 0) * np.pi, np.abs(r), label=label)
pylab.legend(loc="best")
pylab.show()


"""
Demo2  阿基米德落线   r = a+ bθ  不妨a=0，b=1
"""

# a = 0
# b = 1
# theta = np.arange(0, 6, 0.01) * np.pi
# r = a + b * theta
#
# label = "$r={}+{}*\\theta,\\theta\\in[0,6\\pi]$".format(a, b)
# pylab.polar(theta, r, label=label)
# pylab.legend(loc="best")
# pylab.show()
