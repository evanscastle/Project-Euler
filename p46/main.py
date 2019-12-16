import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from number_theory import is_not_prime
from local_methods import prime_plus_twice_square

i = 9
while True:
    if is_not_prime(i):
        temp = prime_plus_twice_square(i)
    if len(temp) == 0:
        break
    else:
        i += 2

print(i)
