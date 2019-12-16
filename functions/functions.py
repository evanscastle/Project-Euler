#to use, add this uncommented statement to the top of a program
# import sys
# sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")
#=====================================================================================
import math

#some useful functions

def nCr(n,r):
    return math.floor(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
















































#============================================================================
#THE FUNCTIONS BELOW THIS LINE HAVE BEEN MOVED TO OTHER FILES IN THE SAME
#DIRECTORY. THEY REMAIN COPIED HERE FOR BACKWARDS COMPATIBILITY OF PYTHON
#CODE. MODIFIED 4/8/2019
#============================================================================

#CURRENTLY IN: number_theory.py

#determines whether a number is prime
def is_prime(n):
    if n <= 0:
        return False
    m = math.floor(math.sqrt(n))
    for i in range(2, m+1):
        if n%i == 0:
            return False
    return True

#returns all prime numbers less than a given value
def primes_leq(n):
    list = []
    for i in range(2,n):
        if is_prime(i):
            list.append(i)
    return list
#============================================================================

#CURRENTLY IN: formattin.py
#return the nth place of a given number, 0 - ones place, 1 - tens etc
def get_place(num, digit):
    if digit < 0:
        raise ValueError('Number does not contain a digit at that place')
    s = str(num)
    array = list(s)
    if digit > len(array)-1:
        return 0
    else:
        return int(array[len(array)-digit-1])

#sums the digits of a given number
def sum_digits(num):
    sum = 0
    s = str(num)
    array = list(s)
    for i in range(0, len(array)):
        sum = sum + int(array[len(array)-i-1])
    return sum

#initializes a vector of a specified size
def initialize_vector(size):
    array = []
    for i in range(0,size):
        array.append(0)
    return array

#initializes an n by m matrix of all zeroes
def initialize_matrix(n,m):
    array = initialize_vector(n)
    for i in range(0,n):
        array[i] = initialize_vector(m)
    return array
