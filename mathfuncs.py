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

""" The factorial function. Takes a positive integer and gives it's facorial (!). """
def factorial(n):
    n1 = 1
    for i in range(n):
        if i > 0:
            n1 = n1 * i
    n1 = n1 * n
    return n1
