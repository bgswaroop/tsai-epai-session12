import numpy as np

from .utils import print_math_op

__all__ = ['softmax']


@print_math_op
def softmax(x):
    normalization_factor = sum([np.exp(y) for y in x])
    return [y / normalization_factor for y in x]


@print_math_op
def derivative_softmax(value, input):
    gradient = [None] * len(value)
    for i in range(len(value)):
        for j in range(len(input)):
            if i == j:
                gradient[i] = value[i] * (1 - input[i])
            else:
                gradient[i] = -value[i] * input[j]
    return gradient
