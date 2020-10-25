import math

from .utils import print_math_op

__all__ = ['sigmoid']


@print_math_op
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


@print_math_op
def derivative_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))
