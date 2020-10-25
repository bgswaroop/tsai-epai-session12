import math

from .utils import print_math_op

__all__ = ['tanh']


@print_math_op
def tanh(x):
    return math.tanh(x)


@print_math_op
def derivative_tanh(x):
    return 1 - tanh(x) ** 2
