import sys
import datetime
sys.path.append("C:/Users/evans/Google Drive/Code/Python/Project Euler/functions")

#code currently executes in approx 264 seconds
from number_theory import *

start = datetime.datetime.now()

#we observe the following pattern in the spiral:
#if the square at the bottom right of the spiral is d^2, then the entries going around are {d^2 - 3*(d-1)}, {d^2 - 2*(d-1)}, {d^2 - (d-1)}, {d^2}
#the total number of entries in level k of the spiral is (2k+1)**2
ratio = 1
num_primes = 0
level = 1

while ratio > 0.1:
    side_length = 2*level + 1
    diagonal_length = 2*side_length - 1 #subtract 1 because center is double counted
    for i in range(1, 4):
        #area - walking perimeter backwards
        if is_prime(side_length**2 - i*(side_length-1)):
            num_primes += 1

    level += 1
    ratio = num_primes/diagonal_length

end = datetime.datetime.now()
duration = (end - start).total_seconds()

print(f'Answer: {2*(level-1) + 1}')
print(f'Elapsed Time: {duration}')
