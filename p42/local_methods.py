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

#determines if the given number is triangular
def is_triangle(num):
    #solves the appropriate quadratic. If the result is integral the given number
    #must be triangular
    root = (-1 + math.sqrt(1+8*num))/2
    if (math.floor(root) == root):
        return True

    else: return False

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

def score(str):
    score = 0
    for i in range(0,len(str)):
        #65 is the ASCII code for 'A'
        score = score + ord(str[i])-64

    return score
