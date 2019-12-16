from functions.number_theory import *

def abundant_numbers_leq(num):
    out = []
    for i in range(2, num):
        if abundant_or_deficient(i) == 1:  # is abundant
            out.append(i)
    return out

def truncate_list(upper_bound, array):  # return a list whose elements do not exceed upper_bound
    out = []
    i = 0
    while i < len(array):
        if array[i] < upper_bound:
            i += 1
        else:
            break

    return array[0:i]

UPPER_LIMIT = 28123

abundant_nums = abundant_numbers_leq(UPPER_LIMIT)

solution = []

for i in range(1, 28124):
    if i % 1000 == 0:
        print(i)

    truncated_list = truncate_list(i, abundant_nums)

    j = 0
    found_pair = False
    while j < len(truncated_list):
        curr = i - truncated_list[j]

        if curr < truncated_list[0]:  # This is redundant because of how we construct the truncated
                                      # list. We could replace the construction of that list with
                                      # this statement, shortening the amount of time the search
                                      # executes. (Not sure if its much faster though)
            break
        else:
            if curr in truncated_list:
                found_pair = True
                break
            else:
                j += 1

    if not found_pair:
        solution.append(i)  # no need for comparator b/c we are searching sequentially

print(f'The sum of all positive integers which cannot be written '
      f'as the sum of two abundant numbers is {sum(solution)}')
