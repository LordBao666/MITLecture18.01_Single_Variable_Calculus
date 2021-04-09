"""
@Author  : Lord_Bao
@Date    : 2021/4/9

"""
import pylab


"""
可视化 constant multiple rules

"""


def get_derivative(fx, x0, dx=1e-5, precision=4):
    """
    :param fx: 单变量函数fx,
    :param x0: 需要求导的x0
    :param dx: delta x ,刻画无穷小量,默认 1e-5
    :param precision: 默认精度为4，比如求导即为为   0.12432  那么默认返回 0.1243
    :return:
    """
    denominator = dx
    nominator = fx(x0 + dx) - fx(x0)
    return round(nominator / denominator, precision)


def with_constant_func(without_constant_func, constant):
    """
    :param without_constant_func:  单变量函数
    :param constant: 常数系数
    :return: 返回 constant * without_constant_func

    e.g  input fx = x^3 ,constant =3 output 3fx ,namely, 3 x^3
    """
    return lambda x: without_constant_func(x) * constant


def shift_y(y_vals, deltay=1):
    """
    :param y_vals: 列表
    :param deltay: shift   delta y
    :return:
    """
    new_y_vals = [deltay + elt for elt in y_vals]
    return new_y_vals


# fx  =  x^2 + 2x  + 1
myfunc_without_constant = lambda x: x ** 2 + 2 * x + 1

"""
构建带常数的函数 ,假设常数为3
现在证明  constant multiple rules
"""
is_shift = True
constant = 3
myfunc_with_constant = with_constant_func(myfunc_without_constant, constant=constant)

x = range(-100, 100, 1)

# 最重要的1part
derivative_with_constant = [get_derivative(myfunc_with_constant, elt) for elt in x]
derivative_without_constant = [constant * get_derivative(myfunc_without_constant, elt) for elt in x]

if is_shift:
    derivative_without_constant = shift_y(derivative_without_constant, deltay=20)

pylab.xlabel("x")
pylab.ylabel("f(x)")
pylab.plot(x, derivative_without_constant, label="$cf'(x)$")
pylab.plot(x, derivative_with_constant, label="$(cf(x))'$")
pylab.legend(loc="best")
pylab.show()
