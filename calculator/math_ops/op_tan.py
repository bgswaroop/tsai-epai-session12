import math

from .utils import print_math_op

__all__ = ['tan']


@print_math_op
def tan(x):
    return math.tan(x)


@print_math_op
def derivative_tan(x):
    return (1 / math.cos(x)) ** 2
