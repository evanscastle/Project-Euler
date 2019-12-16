from local_methods import get_place, digit_to_text, twenty_to_hundred_to_text, teen_to_text, num_to_text_array

num = 1000
total = 0

#determines number of characters between 1 and num
for i in range(1,num+1):
    current_i = num_to_text_array(i)
    for j in range(0,len(current_i)):
        total = total + len(current_i[j])

print(total)
