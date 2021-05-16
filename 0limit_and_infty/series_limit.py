"""
@Author  : Lord_Bao
@Date    : 2021/5/16

"""

import pylab
import math
import numpy as np

"""


"""
# x = range(1, 30)
# x = range(31, 61)
x = range(61, 1000)

y = [((10 / elt) * math.sin(200 / elt) + 1) for elt in x]

gap = [abs(elt - 1) for elt in y]

for i in range(len(x)):
    print("(", x[i], ",", y[i], ")")

pylab.axhline(0, color="grey")
# pylab.axvline(0, color="grey")
# pylab.axhline(1, color="grey", label="A=1")
pylab.xlabel("n")
pylab.ylabel("$a_n$")

# pylab.plot(x, y, ".", label="$a_n=\\frac{10}{n}\\sin(\\frac{200}{n})+1$")
pylab.plot(x, gap, ".", label="$|a_n-A|$")
# 绘制x轴和y轴刻度
# pylab.xticks(x, rotation=-45)
y_min, y_max = pylab.ylim()
# n=1 到 30
# pylab.yticks(np.arange(math.floor(y_min), math.ceil(y_max), 1))
# n=31 到 60
# pylab.yticks(np.arange(math.floor(y_min), math.ceil(y_max), 0.1))

# pylab.axis("equal")
pylab.legend(loc="best")
pylab.show()
