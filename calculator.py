# https://github.com/Jtorresuribe/Lab11-JT-U-RR.git
# Partner 1 Joaquin Torres-Uribe
# Partner 2 Reyhan Rahman
import math


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else: return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0: raise ZeroDivisionError

    else:
        return b/a

def logarithm(a,b):
    if b >= 1:
        return math.log(a, b)
    elif b < 1:
        raise ValueError
    elif a < 1:
        raise ZeroDivisionError


def exp(a,b):
    return a ** b


