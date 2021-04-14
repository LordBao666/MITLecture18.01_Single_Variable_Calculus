"""
@Author  : Lord_Bao
@Date    : 2021/4/10

"""
import pylab
import numpy as np
import math

"""
求  反函数 和 函数的对称图形

"""

# sinθ arcsinθ
theta = np.arange(-3, 3, 0.01) * math.pi
sin_theta = np.array([math.sin(elt) for elt in theta])

pylab.xlabel("$\\theta$")
pylab.ylabel("f($\\theta$)")
pylab.axhline(0, color="grey")
pylab.axvline(0, color="grey")
pylab.axline((0.0, 0.0), slope=1.0, color="black", linestyle="--", label="y=x")
# 比如 x 和 y互换
pylab.plot(theta, sin_theta, label="$\\sin(\\theta)$")
pylab.plot(sin_theta, theta, label="$\\arcsin \\theta$")
pylab.legend(loc="best")
pylab.show()

"""
tanθ arctanθ
"""
# # tanθ arctanθ
# # [start, stop)
# theta = np.arange(-0.40, 0.41, 0.01) * math.pi
# # theta = np.arange(-0.49, 0.50, 0.01) * math.pi
# # theta = np.arange(-0.499, 0.500, 0.001) * math.pi
# tan_theta = np.array([math.tan(elt) for elt in theta])
#
# pylab.xlabel("$\\theta$")
# pylab.ylabel("f($\\theta$)")
# pylab.axhline(0, color="grey")
# pylab.axvline(0, color="grey")
# pylab.axline((0.0, 0.0), slope=1.0, color="black", linestyle="--", label="y=x")
# # pylab.xlim(-40, 40)
# # pylab.ylim(-40, 40)
# # x 和  y 互换
# pylab.plot(theta, tan_theta, label="$\\tan(\\theta)$")
# pylab.plot(tan_theta, theta, label="$\\arctan \\theta$")
# pylab.legend(loc="best")
# pylab.show()
