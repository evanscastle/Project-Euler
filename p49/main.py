import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from formatting import num_to_array, array_to_num, permutations, remove_duplicates
from number_theory import primes_between, is_prime


primes = primes_between(1000,10000)

candidates = []
final = []

for i in primes:
    #takes the current element of primes and outputs a list of all its permutations
    current_array = num_to_array(i)
    curr_perms_arr = permutations(current_array)
    curr_perms = []
    for j in range(0,len(curr_perms_arr)):
        curr_perms.append(array_to_num(curr_perms_arr[j]))

    #determines which if any permutations are prime
    prime_perms = []
    for j in range(0,len(curr_perms)):
        if is_prime(curr_perms[j]) and curr_perms[j] > 1000:
            prime_perms.append(curr_perms[j])

    #formats list
    prime_perms = remove_duplicates(prime_perms)
    prime_perms.sort()

    if(len(prime_perms)) >= 3:
        candidates.append(prime_perms)

candidates = remove_duplicates(candidates)

#find differences among elements of candidates and checks if that difference contains 3330
for i in range(0,len(candidates)):
    diff = []
    for j in range(0,len(candidates[i])):
        k = 1
        while j + k < len(candidates[i]):
            #produces all positive pairwise differences among the elements of candidates[i]
            diff.append(candidates[i][j+k]-candidates[i][j])
            k += 1

    #detects if there is a sequence differing by 3330
    num_times = 0
    for l in range(0,len(diff)):
        if diff[l] == 3330:
            num_times += 1

    if num_times > 1:
        final.append(candidates[i])
        
print(final)
