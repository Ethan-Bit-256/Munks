import math

""" The addition function. You can take any number of arguments and add them. """
def sum(*args):
    result = 0
    for i in args:
        result = result + i
    return result

""" The subtraction function. You can take any number of arguments and subtract them (starting from the first argument). """
def sub(*args):
    number = args[0]

    for i in args[1:]:
        number = number - i
    return number

""" The multiplication function. You can take any number of arguments and multiply them. """
def mul(*args):
    result = 1
    for i in args:
        result = result * i
    return result

""" The division function. You can take any number of arguments and divide them (starting from the fisrt argument). """
def div(*args):
    number = args[0]

    for i in args[1:]:
       number = number / i
    return number 

""" Quadratic Formula with the +. """
def quadformadd(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    root = math.sqrt(abs(discriminant))
    result1 = -b + root
    result1 = result1 / 2 * a

    return result1

""" Quadratic Formula with the -. """
def quadformsub(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    root = math.sqrt(abs(discriminant))
    result1 = -b - root
    result1 = result1 / 2 * a

    return result1

