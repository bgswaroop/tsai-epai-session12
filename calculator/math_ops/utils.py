def print_math_op(func):
    from functools import wraps

    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'\nThe result of the operation {func.__name__} on the input {args} is {result}')
        return result

    return inner
