import sys
import math
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from formatting import num_digits, get_place

num = math.factorial(100)
sum = 0

for i in range(0, num_digits(num)):
    sum = sum + get_place(num, i)

print(sum)
