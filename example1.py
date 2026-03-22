""" This demonstrates the functions in Munks """

from munks import *

print("++++++++++++++++++++")
print("+ Basic Operations +")
print("++++++++++++++++++++\n")
print(f"1 + 2.2 + 3.33 = {sum(1, 2.2, 3.33)}")
print(f"10 - 5 - 3.5 = {sub(10, 5, 3.5)}")
print(f"3 * 4.5 * 2 = {mul(3, 4.5, 2)}")
print(f"40 / 100 / 2 = {div(40, 100, 2)}\n")

print("++++++++++++++++++++++++++++++++++++++++++++")
print("+ Factorials, Combinations, & Permutations +")
print("++++++++++++++++++++++++++++++++++++++++++++\n")
print(f"5! = {factorial(5)}")
print(f"10C5 = {combination(10, 5)}")
print(f"6P4 = {permutation(6, 4)}\n")

print("+ Inverse +\n")
print(f"40-1(inverse) = {inverse(40)}\n")

""" The data set for demonstrating the statistical functions """
test_dataset = [-3, -2.5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("+++++++++++++++++++++++++")
print("+ Statistical Functions +")
print("+++++++++++++++++++++++++\n")
print(f"The data set: (-3, -2.5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), has a mean of           {mean(*test_dataset)}")
print(f"The data set: (-3, -2.5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), has a variance of       {variance(*test_dataset)}")
print(f"The data set: (-3, -2.5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), has a std_deviation of  {std_deviation(*test_dataset)}\n")
