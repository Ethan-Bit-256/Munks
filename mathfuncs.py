def add(*args):
    result = 0
    for i in args:
        result = result + i
    return result

def sub(*args):
    number = args[0]

    for i in args[1:]:
        number = number - i
    return number

def mul(*args):
    result = 1
    for i in args:
        result = result * i
    return result

def div(*args):
    number = args[0]

    for i in args[1:]:
       number = number / i
    return number 

