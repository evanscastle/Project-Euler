file = open ("numbers.txt", "r")
rows = file.readlines()

array = []
#converts array.txt into an actual array
for i in range(0, len(rows)):
    current_line = rows[i].rstrip() #removes new line
    array.append(current_line)

#replace string array with int
for i in range(0, len(array)):
         array[i] = int(array[i]) #convert array to ints

sum = 0
for i in range(0, len(array)):
    sum = sum + array[i]

print(sum)
