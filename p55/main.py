import sys
import datetime
sys.path.append("C:/Users/evans/Google Drive/Code/Python/Project Euler/functions")

#code currently executes in approx 264 seconds
from formatting import *

start = datetime.datetime.now()

#can stop at 50 iterations
count = 0

num = 0
while num < 10000:
    sum = num
    halt_search = False
    i = 0
    while i < 50 and not halt_search:
        mus = array_to_num(reverse_array(num_to_array(sum)))
        sum = sum + mus

        if is_palindrome(sum):
            halt_search = True

        if not halt_search:
            i += 1

    #if we make it all the way through, assume Lychrel
    if i == 50:
        count += 1

    num += 1

end = datetime.datetime.now()
duration = (end - start).total_seconds()
print(f'Lychrel: {count}')
print(f'elapsed time: {duration}')
