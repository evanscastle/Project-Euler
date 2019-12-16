#to use, add this uncommented statement to the top of a program
# import sys
# sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")
#=====================================================================================
#The functions below are included as useful methods for formatting numbers
#and initializing useful data structures to work with problems common to
#Project Euler

#returns the number of digits in an integer
def num_digits(num):
    s = str(num)
    return len(s)

#return the nth place of a given number, 0 - ones place, 1 - tens etc
def get_place(num, digit):
    s = str(num)
    array = list(s)
    return int(array[len(array)-digit-1])

#sums the digits of a given number
def sum_digits(num):
    sum = 0
    s = str(num)
    array = list(s)
    for i in range(0, len(array)):
        sum = sum + int(array[len(array)-i-1])
    return sum

#converts a given number to an array consisting of its digits
def num_to_array(num):
    s = str(num)
    array = list(s)
    for i in range(0, len(array)):
        array[i] = int(array[i])
    return array

def reverse_array(array):
    new = []
    for i in range(0, len(array)):
        new.append(array[len(array)-1-i])

    return new

#takes in a number as an array of digits and converts it to an int
def array_to_num(array):
    num = 0
    for i in range(0, len(array)):
        num = num + array[i]*10**(len(array)-i-1)
    return num

#returns an array whose elements are all of the permutations of the elements of the input array
def permutations(array):
    out = []
    #base case
    if len(array) == 0:
        return []

    if len(array) == 1:
        return [array]
    #recursion
    for i in range(len(array)):
        current = array[i]

        array_copy = list(array) #copy array and pass to permutations. If we modify
        array_copy.pop(i)        #the original array, we lose data when we loop

        for j in permutations(array_copy):
            out.append([current] + j)

    return out

#removes duplicates from a list
#could make a dictionary and then cast back to list
def remove_duplicates(array):
    array.sort()

    j = 0
    while j < len(array) - 1: #global counter recording the number of distinct elements in the array
        if (array[j] == array[j+1]):
            array.pop(j+1)
        else:
            j += 1
    return array

def is_palindrome(num):
    array = num_to_array(num)

    i = 0
    while i < len(array)/2:
        if array[i] != array[len(array)-1-i]:
            return False
        i += 1

    #if we get all the way through, return true
    return True

#initializes a vector of a specified size
def initialize_vector(size):
    array = []
    for i in range(0,size):
        array.append(0)
    return array

#initializes an n by m matrix of all zeroes
def initialize_matrix(n,m):
    array = initialize_vector(n)
    for i in range(0,n):
        array[i] = initialize_vector(m)
    return array

def cyclic_permutations(num):
    array = num_to_array(num)

    out = []
    for i in range(0, len(array)):
        curr = array_to_num(array[i:len(array)] + array[0:i])
        out.append(curr)

    return out


