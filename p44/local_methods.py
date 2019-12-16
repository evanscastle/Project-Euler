import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

import math

#returns the appropriate pentagonal number
def pentagon(num):
    return int(num*(3*num-1)/2)

#checks if a number is pentagonal
def is_pentagonal(num):
    #solve the quadratic, if it's an integer, it must be pentagonal
    solution = (1 + (math.sqrt(1+24*num)))/6
    if math.floor(solution) == solution:
        return True
    else:
        return False

def get_pent_between(num1, num2):
    if num1 <= 0:
        num1 = 1

    lower = math.floor((1 + (math.sqrt(1+24*num1)))/6)
    upper = math.floor((1 + (math.sqrt(1+24*num2)))/6) + 1

    array = []
    for i in range(lower, upper):
        array.append(pentagon(i))
    return array
