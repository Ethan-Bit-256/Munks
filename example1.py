""" This demonstrates the functions in Munks """

from munks import *

print(f"1 + 2.2 + 3.33 = {sum(1, 2.2, 3.33)}")
print(f"10 - 5 - 3.5 = {sub(10, 5, 3.5)}")
print(f"3 * 4.5 * 2 = {mul(3, 4.5, 2)}")
print(f"40 / 100 / 2 = {div(40, 100, 2)}")
print(f"5! = {factorial(5)}")
print(f"10C5 = {combination(10, 5)}")
print(f"6P4 = {permutation(6, 4)}")
print(f"40-1(inverse) = {inverse(40)}")
print(f"Data set: '1, 2.5, 3, 4, 8, 11.38, 5.2' has a mean of {mean(1, 2.5, 3, 4, 8, 11.38, 5.2)}.")
