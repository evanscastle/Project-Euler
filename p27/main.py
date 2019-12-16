from functions.number_theory import *

def poly(n, a, b):
    return n**2 + a * n + b

best_count = 0
best_a = None
best_b = None

for a in range(-1000, 1001):
    # if a % 100 == 0:
    #     print(a)

    for b in range(-1000, 1001):

        n = 0
        while is_prime(poly(n, a, b)):
            n += 1

        if n > best_count:
            best_a = a
            best_b = b
            best_count = n

print(f'The polynomial n^2 + {best_a}n + {best_b} produces {best_count + 1} consecutive primes')
print(f'Product of coefficients: {best_a * best_b}')