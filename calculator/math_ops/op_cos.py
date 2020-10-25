import math

from .utils import print_math_op

__all__ = ['cos']


@print_math_op
def cos(x):
    return math.cos(x)


@print_math_op
def derivative_cos(x):
    return -math.sin(x)
