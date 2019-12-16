import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from number_theory import primes_leq, is_prime, divisors, first_n_primes

#this algorithm performs a top-down search of sequences of consecutive primes
#by first establishing an upper bound on the length of a chain of primes whose
#sum is less than a given max. It then shortens the length of the chain
#and shifts it until the first prime is found less than the given max.
#This data is then output to the screen with the length of the chain, the starting
#position, and the prime which witnesses the selection criteria


max = 1000000
sum = 0
bound = 0
primes = first_n_primes(600)
#finds an upper bound on longest possible length of a list of consecutive
#primes whose sum is less than max
while sum < max:
    sum = sum + primes[bound]
    bound = bound + 1

array = []

while True:
    bound = bound - 1 #narrow maximum width of search
    shift = 0 #reinitialize shift
    #NOTE: array should not need reinitialized because this code only executes if it's empty
    print("bound = ", bound)
    while True:
        candidate = 0
        #add up the primes between index j and bound + j to produce a candidate
        for k in range(shift, bound + shift):
            candidate = candidate + primes[k]

        if candidate <= max and is_prime(candidate): #if candidate meets selection criteria, record it
            array.append(candidate)
            shift = shift + 1
            print(candidate,' - candidate added')
        elif candidate <= max:
            shift = shift + 1
            print(candidate,' - candidate was not prime')
        else:
            print(candidate,' - candidate overstepped bounds')
            break
    print('while loop finished', "\n\n")

    #detects if the inner loop found any candidates
    if len(array) > 0:
        array.sort()
        largest = array[len(array)-1] #picks out largest element which is prime
        data = [bound, shift, largest] #[number of terms, starting index, prime picked]
        break
    if bound == 0:
        break

print(data)
