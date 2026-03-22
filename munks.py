"""
   Munks 0.2.0
"""

""" Required Import """
from math import *

""" Some mathematical constants """
pi = 3.141592653589793      # Pi (15 decimal places)
eul = 2.718281828459045     # Euler's Number (15 decimal places)

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

""" The inverse function. Takes one argument (number x), and gives its inverse (x-1). """
def inverse(x):
    result = 1/x
    return result

""" The mean function. Enter as many arguments as you like and it'll give you the average. """
def mean(*args):
    total = 0             # *args summed up
    count = 0             # the number of arguments passed

    for i in args:        # going through the passed arguments
        total+=i          # adding up the arguments
        count+=1          # finding out the number of arguments passed

    result = total/count  # calculating the average

    return result         # returning the average of *args

""" The variance function. Enter as many arguments as you like and it'll return their variance. """
def variance(*args):
    count = 0                      # Number of values
    values = []                    # Here, we'll store the values in args after they've each been squared

    avg = mean(*args)              # Mean of args
    avgsq = avg*avg                # Squaring the mean

    for i in args:

        currentvar = i*i           # Squaring each value in args
        values.append(currentvar)  # Adding the squared values to the list of squared values

        count+=1                   # Counting the number of values in args

    sum_of_xsq = sum(*values)      # Summing our squared values to be used in the equation(xsq stands for "x squared")

    part1 = sum_of_xsq/count       # The quotient of sum_of_xsq and the number of values

    result = part1 - avgsq         # Our final result which we get by subtracting the square of our average from part1.

    return result

""" The standard deviation function. Enter as many arguments as you like and it'll return their standard deviation. I appreciate how easy this function was to write. """
def std_deviation(*args):
    return sqrt(variance(*args))   # Standard deviation is just the square root of variance.

