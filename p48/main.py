import sys
import time
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

#code currently executes in approx 264 seconds
from local_methods import has_n_distinct_factors

#global variable used to identify number of sequential integers with given property desired
SEQUENCE_TARGET = 4

i = 2
counter = 0
while True:
    if has_n_distinct_factors(SEQUENCE_TARGET, i):
        counter += 1
    else:
        counter = 0

    if (counter >= SEQUENCE_TARGET):
        break
    i += 1
    if i%10000 == 0:
        print(i)

for j in range(0, SEQUENCE_TARGET):
    #prints the desired sequence of numbers
    print(i + j - (SEQUENCE_TARGET - 1))
