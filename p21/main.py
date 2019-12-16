import sys
import math
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from number_theory import divisors, proper_divisors, is_perfect_sq

#generate a list of all numbers from 1 to 10000
#if a number is not amicable, remove it from the list

num = 10000
amicable_numbers = []

#finds all amicable numbers below 10000
for i in range(2,num):

    current_divisors = proper_divisors(i)
    sum_current_divisors = 0

    for j in range(0, len(current_divisors)):
        sum_current_divisors = sum_current_divisors + current_divisors[j]

    #establishes the candidate for the amicable pair
    partner = sum_current_divisors
    partner_divisors = proper_divisors(partner)
    sum_partner_divisors = 0

    for j in range(0, len(partner_divisors)):
        sum_partner_divisors = sum_partner_divisors + partner_divisors[j]

    #determines if the pair is amicable and checks if number is perfect (i.e. not amicable))
    if sum_partner_divisors ==  i and i != partner:
        amicable_numbers.append(i)
        amicable_numbers.append(partner)

#Creates a dictionary with keys consisting of elements from list. Since dictionary
#cant have duplicates, removes duplicate amicable pairs
amicable_numbers = list(dict.fromkeys(amicable_numbers))
amicable_numbers.sort()

print(amicable_numbers)

sum = 0
for i in range(0, len(amicable_numbers)):
    if amicable_numbers[i] < num:
        sum = sum + amicable_numbers[i]

print(sum)
