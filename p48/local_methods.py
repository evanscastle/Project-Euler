import sys
import math
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

#a more efficient, problem specific algorithm for finding a sequence of numbers
#with a given factorization than actually factoring every number

def has_n_distinct_factors(n, num):
    counter = 0
    i = 2
    reduced = num

    #could improve this function by only searching on i which are prime
    while counter < n and reduced > 1:
        if(reduced%i == 0):
            counter += 1
            #remove the prime divisior from the search
            while(int(reduced%i) == 0):
                reduced = int(reduced/i)
        i += 1

    if counter >= n:
        return True
    else:
        return False
