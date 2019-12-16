import sys
import gc
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from formatting import permutations, array_to_num

#Code currently executes in 31.2 seconds

array = [0,1,2,3,4,5,6,7,8,9]
list = []
perms = permutations(array)

for i in range(0, len(perms)):
    if array_to_num(perms[i][1:4])%2 == 0:
        if array_to_num(perms[i][2:5])%3 == 0:
            if array_to_num(perms[i][3:6])%5 == 0:
                if array_to_num(perms[i][4:7])%7 == 0:
                    if array_to_num(perms[i][5:8])%11 == 0:
                        if array_to_num(perms[i][6:9])%13 == 0:
                            if array_to_num(perms[i][7:10])%17 == 0:
                                list.append(array_to_num(perms[i]))

sum = 0
for i in range(0, len(list)):
    sum = sum + list[i]

print(sum)
