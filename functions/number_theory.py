#to use, add this uncommented statement to the top of a program
# import sys
# sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")
#=====================================================================================

#this file contains methods which are used to discern interesting properties of integers

import math

#determines whether a number is prime
def is_prime(num):
    if num <= 1:
        return False
    num = abs(num)
    m = math.floor(math.sqrt(num))
    for i in range(2, m+1):
        if num%i == 0:
            return False
    return True

#determines whether a number is composite
def is_not_prime(num):
    num = abs(num)
    m = math.floor(math.sqrt(num))
    for i in range(2, m+1):
        if num%i == 0:
            return True
    return False

#returns all prime numbers less than a given value
def primes_leq(num):
    list = []
    for i in range(2,num):
        if is_prime(i):
            list.append(i)
    return list

def first_n_primes(num):
    i = 2
    array = []
    while True:
        if is_prime(i):
            array.append(i)
        if len(array) >= num:
            break
        i = i + 1

    return array

#returns prime numbers between num1 and num2, inclusive
def primes_between(num1, num2):
    list = []
    for i in range(num1, num2 + 1):
        if is_prime(i):
            list.append(i)
    return list

#method to determine if a given integer is a perfect square
def is_perfect_sq(num):
    sqrt_num = math.sqrt(num)
    if (sqrt_num == math.floor(sqrt_num)):
        return True
    else:
        return False

#lists divisors of a number
def divisors(num):
    #allows for negative inputs
    num = abs(num)

    if num == 1:
        return [1]

    array = []
    if is_perfect_sq(num):
        m = math.floor(math.sqrt(num))
        for i in range(1, m):
            if num%i == 0:
                array.append(i)
                array.append(int(num/i))
        array.append(m)
    else:
        m = math.floor(math.sqrt(num))
        for i in range(1, m+1):
            if num%i == 0:
                array.append(i)
                array.append(int(num/i))
    array.sort()
    return array

#lists proper divisors of a number
def proper_divisors(num):
    array = list(divisors(num))
    array.pop()
    return array

#sum proper divisors, -1 if deficient, 0 if perfect, 1 if abundant
def abundant_or_deficient(num):
    divisors = proper_divisors(num)
    if sum(divisors) < num:
        return -1
    if sum(divisors) == num:
        return 0
    if sum(divisors) > num:
        return 1

#returns the prime factorization of a number
#AT SOME POINT MAKE A RECURSIVE VERSION WITH TREES
def factor(num):
    out = []
    current = num
    i = 2
    while current > 1:
        #if a divisor is found, add to list and shorten search
        if current%i == 0:
            out.append(i)
            current = math.floor(current/i)
            i = 2
        else:
            i += 1
    return out
