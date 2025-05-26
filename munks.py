"""
   Munks 0.0.2
"""

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

""" The factorial function. Takes an integer and gives it's facorial (!). """
def factorial(n):
    n1 = 1
    for i in range(abs(n)):
        if i > 0:
            n1 = n1 * i
    n1 = n1 * n
    return n1

""" The combination function. Takes two arguments (n & r) and gives their combination (nCr). """
def  combination(n, r):
    facn = factorial(n)                      # facn means "factorial of n"
    nminr = n - r                            # nminr means "n minus r"
    facnminr = factorial(nminr)              # facnminr means "factorial of the result of n minus r"
    facr = factorial(r)                      # facr means "factorial of r"
    denominator = facr * facnminr            # denominator is what we'll be dividing facn by in order to get the result
    result = facn / denominator

    return int(result)

""" The permutation function. Takes two arguments (n & r) and gives their permutation (nPr). """
def permutation(n, r):
    facn = factorial(n)                  # facn means "factorial of n"
    facnminr = factorial(n - r)          # facnminr means "factorial of n minus r"
    result = int(facn / facnminr)        # the final result
    return result
