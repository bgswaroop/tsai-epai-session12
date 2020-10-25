import math

from .utils import print_math_op

__all__ = ['sin']


@print_math_op
def sin(x):
    return math.sin(x)


@print_math_op
def derivative_sin(x):
    return math.cos(x)
