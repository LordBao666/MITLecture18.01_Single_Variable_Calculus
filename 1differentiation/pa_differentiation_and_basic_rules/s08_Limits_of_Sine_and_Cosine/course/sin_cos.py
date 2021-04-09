"""
@Author  : Lord_Bao
@Date    : 2021/4/9

"""
import pylab
import numpy as np
import math

"""
求  sinθ/θ   和 cosθ - 1/ θ 的比值


"""
"""
sinθ/θ  

"""
# 函数
# # theta = np.arange(-0.1, 0.1, 0.001) * math.pi
# theta = np.arange(-1, 1, 0.01) * math.pi
# sin_theta = np.array([math.sin(elt) for elt in theta])
# ratio_of_edge_to_arc = sin_theta / theta
#
# pylab.xlabel("$\\theta$")
# pylab.ylabel("f($\\theta$)")
# pylab.plot(theta, theta, label="$\\theta$")
# pylab.plot(theta, sin_theta, label="$\\sin(\\theta)$")
# pylab.plot(theta, ratio_of_edge_to_arc, label="$\\frac{\\sin(\\theta)} {\\theta}$")
# pylab.axhline(1, label="y=1")
# pylab.legend(loc="best")
# pylab.show()

"""
cosθ - 1/ θ
"""

# 函数
# theta = np.arange(-0.01, 0.01, 0.0001) * math.pi
# theta = np.arange(-0.1, 0.1, 0.001) * math.pi
theta = np.arange(-1, 1, 0.01) * math.pi
one_minus_cos_theta = np.array([1- math.cos(elt) for elt in theta])
ratio_of_edge_to_arc = one_minus_cos_theta / theta

pylab.xlabel("$\\theta$")
pylab.ylabel("f($\\theta$)")
pylab.plot(theta, theta, label="$\\theta$")
pylab.plot(theta, one_minus_cos_theta, label="$1-\\cos(\\theta)$")
pylab.plot(theta, ratio_of_edge_to_arc, label="$\\frac{1-\\cos(\\theta)} {\\theta}$")
pylab.axhline(0, label="y=0")
# pylab.ylim(-3,3)
pylab.legend(loc="best")
pylab.show()