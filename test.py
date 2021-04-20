import sys

print(sys.version)


def add_2(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'we added 2 to the result of {original_function.__name__} function')
        print(f'The result of the original function is {original_function(*args, **kwargs)}')
        return original_function(*args, **kwargs) + 2
    return wrapper_function


@add_2
def divide(x, y):
    return x / y


print(divide(4, 2))


@add_2
def mul(x, y):
    return x * y


print(mul(4, 2))


@add_2
def add(x, y):
    return x + y


print(add(4, 2))
