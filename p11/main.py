from functions import find_horz, find_vert, find_prod_southeast, find_prod_southwest

file = open ("array.txt", "r")

array = []

rows = file.readlines()

#converts array.txt into an actual array
for i in range(0, len(rows)):
    current_line = rows[i].rstrip() #removes new line
    split = current_line.split(" ")
    array.append(split)

#replace string array with int
for i in range(0, len(array)):
    for j in range(0, len(array[i])):
         array[i][j] = int(array[i][j]) #convert array to ints

a = find_horz(array)
b = find_vert(array)
c = find_prod_southeast(array)
d = find_prod_southwest(array)

print(max(a,b,c,d))
