from functions.formatting import *
from functions.number_theory import *

circular_primes = []
for i in range(1, 1000000):
    if is_prime(i):
        if i % 10000 == 0:
            print(i)

        perms = cyclic_permutations(i)

        j = 0
        while j < len(perms):
            if is_prime(perms[j]):
                j += 1
            else:
                break

        if j == len(perms):
            for num in perms:
                if num not in circular_primes:
                    circular_primes.append(num)

print('Number of circular primes less than 1 million: ' + str(len(circular_primes)))
