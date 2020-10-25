import math

from .utils import print_math_op

__all__ = ['log']


@print_math_op
def log(x):
    return math.log(x)


@print_math_op
def derivative_log(x):
    return 1 / x
