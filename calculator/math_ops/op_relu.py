from .utils import print_math_op

__all__ = ['relu']


@print_math_op
def relu(x):
    if x >= 0:
        return x
    else:
        return 0


@print_math_op
def derivative_relu(x):
    if x > 0:
        return 1
    else:
        return 0
