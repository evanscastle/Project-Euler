import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from local_methods import triangle, is_triangle, get_tri_between, score

#The longest word in the English language is: Pneumonoultramicroscopicsilicovolcanoconiosis
#which has 45 letters. Thus for this problem we only need to generate the triangular numbers
#below 26*45 = 1170

file = open("words.txt", "r")
str = file.read()

words = str.split(",")

for i in range(0, len(words)):
    #removes quotation marks
    words[i] = words[i][1:len(words[i])-1]

tri_nums = get_tri_between(1,1170)
tri_words = []

for i in range(0, len(words)):
    scor = score(words[i])
    if scor in tri_nums:
        tri_words.append(words[i])

print(len(tri_words))
