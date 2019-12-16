import sys
import datetime
sys.path.append("C:/Users/evans/Google Drive/Code/Python/Project Euler/functions")

#code currently executes in approx 264 seconds
from formatting import num_to_array

start = datetime.datetime.now()

#only need to scan from 1000... to 1666... because otherwise 6x will contain too many digits
found = False
n = 1
while not found:
    print(n)
    curr = 10**n
    while curr < 10**(n+1)/6:
        curr_array = num_to_array(curr)
        curr_array.sort()

        bad_match = False
        i = 2
        while i < 7 and not bad_match:
            curr_multiple = curr*i
            curr_multiple_array = num_to_array(curr_multiple)
            curr_multiple_array.sort()

            j = 0
            while j < len(curr_array) and not bad_match:
                if curr_array[j] != curr_multiple_array[j]:
                    bad_match = True
                j += 1
            i += 1

        #upon exiting loop, check to see if both inner loops finished. if so, then we have found desired number
        if i == 7 and j == len(curr_array):
            found = True
            ans = curr

        curr += 1
    n += 1

print(ans)

end = datetime.datetime.now()
duration = (end - start).total_seconds()

print(f'elapsed time: {duration}')
