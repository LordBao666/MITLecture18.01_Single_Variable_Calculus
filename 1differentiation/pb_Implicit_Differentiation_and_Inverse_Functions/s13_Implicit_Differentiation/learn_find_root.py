"""
@Author  : Lord_Bao
@Date    : 2021/4/11

"""
from scipy import optimize
import numpy as np

"""
root(fun, x0, args=(), method='hybr', jac=None, tol=None, callback=None, options=None)
    Find a root of a vector function.
    
    Parameters
    ----------
    fun : callable
        A vector function to find a root of.
    x0 : ndarray
        Initial guess.
    args : tuple, optional
        Extra arguments passed to the objective function and its Jacobian.
    method : str, optional
        Type of solver. Should be one of
    
  Returns
    -------
    sol : OptimizeResult
        The solution represented as a ``OptimizeResult`` object.
        Important attributes are: ``x`` the solution array, ``success`` a
        Boolean flag indicating if the algorithm exited successfully and
        ``message`` which describes the cause of the termination. See
        `OptimizeResult` for a description of other attributes.

"""

"""
测试1
"""
# def func(vals):
#     """
#     :param vals:  列表
#     """
#     return \
#         vals[0] - vals[1], \
#         vals[0] + vals[1] - 2
#
#
# # initial guess 必须是ndarry对象，必传参数
# sol = optimize.root(func, np.array([0, 0]))
# # x[0],x[1] 的顺序和vals[0],vals[1]一一对应
# print("y={}".format(sol.x[0]))
# print("x={}".format(sol.x[1]))

"""
测试2
"""
# def func2(x):
#     # 单变量 如此即可 不一定是 x[0]
#     return x ** 2 - 1
#
#
# # initial guess  是 3,代表猜测是3附近的答案，也就是说  -1 和 1我拿到的是正数这个解
# sol = optimize.root(func2, np.array([3]))
# # x[0]  对应上面的x
# print("x1={}".format(sol.x[0]))
# # initial guess  是 -3,代表猜测是-3附近的答案，也就是说  -1 和 1我拿到的是负数这个解
# sol = optimize.root(func2, np.array([-3]))
# # x[0]  对应上面的x
# print("x2={}".format(sol.x[0]))

"""
测试3
"""


def func3(x, y):
    return x ** 2 - y


y = -3
sol = optimize.root(func3, np.array([3]), (y,))
if sol.success:
    print("x={}".format(sol.x[0]))
else:
    print(sol.message)


