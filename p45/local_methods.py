import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

import math
#NOTES: triangular numbers grow as .5n^2, pentagonal as 1.5n^2, hex as 2n^2, so
# for the purpose of comparison we dont need to generate as many hexagonal numbers

#all of these numbers are generated quadratically so we can explicitly solve the equations
#n(n+1)/2 = num1, num2, etc.

#generates triangular number num
def triangle(num):
    return int(num*(num+1)/2)

def pentagon(num):
    return int(num*(3*num-1)/2)

def hexagon(num):
    return int(num*(2*num-1))

#returns all triangular numbers which are between the given entries
def get_tri_between(num1, num2):
    if num1 <= 0:
        num1 = 1

    #lower and upper bounds on the values of n which will produce values between the given range
    lower = math.floor((-1 + (math.sqrt(1+8*num1)))/2)
    upper = math.floor((-1 + (math.sqrt(1+8*num2)))/2) + 1

    array = []
    for i in range(lower, upper):
        array.append(triangle(i))
    return array

def get_pent_between(num1, num2):
    if num1 <= 0:
        num1 = 1

    lower = math.floor((1 + (math.sqrt(1+24*num1)))/6)
    upper = math.floor((1 + (math.sqrt(1+24*num2)))/6) + 1

    array = []
    for i in range(lower, upper):
        array.append(pentagon(i))
    return array

def get_hex_between(num1, num2):
    if num1 <= 0:
        num1 = 1

    lower = math.floor((1 + (math.sqrt(1+8*num1)))/4)
    upper = math.floor((1 + (math.sqrt(1+8*num2)))/4) + 1

    array = []
    for i in range(lower, upper):
        array.append(hexagon(i))
    return array
