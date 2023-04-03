import numpy as np


def sinus_derivative(x: float, derivative_order: int):
    if derivative_order % 4 == 0:
        return np.sin(x)
    elif derivative_order % 4 == 1:
        return np.cos(x)
    elif derivative_order % 4 == 2:
        return -np.sin(x)
    else:
        return -np.cos(x)


def sinus_taylor(x: float, a: float, degree: int):
    value = np.sin(a)
    for n in range(1, degree + 1):
        value += sinus_derivative(a, n) / np.math.factorial(n) * (x - a)**n
    return value 
