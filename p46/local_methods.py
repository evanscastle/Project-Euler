import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from number_theory import is_prime

def prime_plus_twice_square(num):
    i = 1
    while num > 2*(i**2):
        candidate = num - 2*(i**2)
        if is_prime(candidate):
            return [candidate, i]
        else:
            i += 1
    return []
