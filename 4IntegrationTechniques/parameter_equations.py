"""
@Author  : Lord_Bao
@Date    : 2021/5/8

"""
import pylab
import numpy as np
import math

# """
# Demo1  x=R+rcos t,y=rsin t .t的范围在[0,2pi]
#
# 不妨 R =5  ,r=3
# """
# R = 5
# r = 3
# t = np.arange(0, 2, 0.01) * math.pi
#
# x = [(R + r * math.cos(elt)) for elt in t]
# y = [(r * math.sin(elt)) for elt in t]
# # for i in range(len(x)):
# #     print("(", x[i], ",", y[i], ")")
# pylab.axhline(0, color="grey", label="x")
# pylab.axvline(0, color="grey", label="y")
# pylab.xlabel("x")
# pylab.ylabel("y")
# pylab.plot(x, y, label="$(x-R)^2+y^2=r^2$")
# pylab.legend(loc="best")
# pylab.axis("equal")
# pylab.show()
"""
Demo2  x=tcos t,y=tsin t .t的范围在[0,4pi]

"""

# t = np.arange(0, 4, 0.01) * math.pi
#
# x = [(elt * math.cos(elt)) for elt in t]
# y = [(elt * math.sin(elt)) for elt in t]
#
# pylab.axhline(0, color="grey", label="x")
# pylab.axvline(0, color="grey", label="y")
# pylab.xlabel("x")
# pylab.ylabel("y")
# pylab.plot(x, y, label="$x=t \\cos t ,y=t\\sin t$")
# pylab.legend(loc="best")
# pylab.axis("equal")
# pylab.show()

"""
Demo3  y(t) = -4.9t^2+5,x(t)=t。 t范围为0到1

"""

t = np.arange(0, math.sqrt(5 / 4.9), 0.01)

x = [elt for elt in t]
y = [(-4.9 * (elt * elt) + 5) for elt in t]
for i in range(len(x)):
    print("(", x[i], ",", y[i], ")")

pylab.axhline(0, color="grey")
pylab.axvline(0, color="grey")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.plot(x, y)
pylab.axis("equal")
pylab.show()
