def find_horz(my_array):
    prod = 0
    for i in range(0, len(my_array)): #iterate through rows
        for j in range(0, len(my_array[i])):#iterate through columns

            temp_prod = 1
            if j+3 < len(my_array[i]):#ensure array not overstepping
                for k in range(0,4):#compute product of next 4 numbers
                    temp_prod = temp_prod * my_array[i][j+k]
            else: temp_prod = 0

            if temp_prod > prod:
                prod = temp_prod
    return prod

def find_vert(my_array):
    prod = 0
    for i in range(0, len(my_array)): #iterate through rows
        for j in range(0, len(my_array[i])):#iterate through columns

            temp_prod = 1
            if i+3 < len(my_array):#ensure array not overstepping
                for k in range(0,4):#compute product of next 4 numbers
                    temp_prod = temp_prod * my_array[i+k][j]
            else: temp_prod = 0

            if temp_prod > prod:
                prod = temp_prod
    return prod

def find_prod_southeast(my_array):
    prod = 0
    for i in range(0, len(my_array)): #iterate through rows
        for j in range(0, len(my_array[i])):#iterate through columns

            temp_prod = 1
            if i+3 < len(my_array) and j+3 < len(my_array[i]):#ensure array not overstepping
                for k in range(0,4):#compute product of next 4 numbers
                    temp_prod = temp_prod * my_array[i+k][j+k]
            else: temp_prod = 0

            if temp_prod > prod:
                prod = temp_prod
    return prod

def find_prod_southwest(my_array):
    prod = 0
    for i in range(0, len(my_array)): #iterate through rows
        for j in range(0, len(my_array[i])):#iterate through columns

            temp_prod = 1
            if i-3 >= 0  and j+3 < len(my_array[i]):#ensure array not overstepping
                for k in range(0,4):#compute product of next 4 numbers
                    temp_prod = temp_prod * my_array[i-k][j+k]
            else: temp_prod = 0

            if temp_prod > prod:
                prod = temp_prod
    return prod





def find_max_product(my_array):
    return my_array[0][0]
