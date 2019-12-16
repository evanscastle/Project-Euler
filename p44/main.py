import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from local_methods import pentagon, is_pentagonal

pairs = []
diffs = []

i = 1
while True:
    j = 1
    while j < i:
        current = pentagon(i) - pentagon(j)
        if is_pentagonal(current):
            current = pentagon(i) + pentagon(j)
            if is_pentagonal(current):
                pairs.append([pentagon(j), pentagon(i)])
                diffs.append(pentagon(i) - pentagon(j))
        j += 1
    #since our function is convex, we will know that we have found the minimum when
    #P_i - P_(i-1) is bigger than some difference we found
    # if (len(pairs) > 0) and ((pentagon(i) - pentagon(i-1)) > min(diffs)):
    #     break

    #NOTE: While the above statement guarantees that we have found the minimum, it is
    #extremely computationally expensive because the pentagonal numbers only grow quadratically
    #so their successive differences grow linearly. In the interest of brevity, the above
    #statement will be shortened to omit the second condition so the loop halts upon
    #finding the first successful candidate

    if (len(pairs) > 0):
        break
    i += 1

print(diffs)
