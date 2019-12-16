import sys
import datetime
sys.path.append("C:/Users/evans/Google Drive/Code/Python/Project Euler/functions")

#code currently executes in approx 264 seconds
from formatting import *

start = datetime.datetime.now()

#we observe the following pattern in the continued fractions:
#3/2, 7/5, 17/12, 41/29, ...
#each successive numerator is 2*(d-1) + (n-1) and each successive denominator is (d-1) + (n-1)
#we will proceed along this course without proof that the above pattern holds (although it seems likely given the continued fraction expansion of sqrt 2)

count = 0

numer = 3
denom = 2
for i in range(0, 1001):
    numer_copy = numer
    numer = 2*denom + numer
    denom = denom + numer_copy

    if num_digits(numer) > num_digits(denom):
        count += 1

end = datetime.datetime.now()
duration = (end - start).total_seconds()

print(f'Count: {count}')
print(f'elapsed time: {duration}')
