import math

from .utils import print_math_op

__all__ = ['exp']


@print_math_op
def exp(x):
    return math.exp(x)


@print_math_op
def derivative_exp(x):
    return math.exp(x)
