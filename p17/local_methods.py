#return the nth place of a given number, 0 - ones place, 1 - tens etc
def get_place(num, digit):
    if digit < 0:
        raise ValueError('Number does not contain a digit at that place')
    s = str(num)
    array = list(s)
    if digit > len(array)-1:
        return 0
    else:
        return int(array[len(array)-digit-1])

#converts a digit to its English text representation
def digit_to_text(num):
    num = num
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'
    else: raise ValueError('Digit 0 through 9 expected')

#converts a number between 10 and 19 inclusive to its English text representation
def teen_to_text(num):
    num = num
    if num == 10:
        return 'ten'
    elif num == 11:
        return 'eleven'
    elif num == 12:
        return 'twelve'
    elif num == 13:
        return 'thirteen'
    elif num == 14:
        return 'fourteen'
    elif num == 15:
        return 'fifteen'
    elif num == 16:
        return 'sixteen'
    elif num == 17:
        return 'seventeen'
    elif num == 18:
        return 'eighteen'
    elif num == 19:
        return 'nineteen'
    else: raise ValueError('Number 10 through 19 expected')

def twenty_to_hundred_to_text(num):
    num = num
    array = []
    if num >= 20 and num < 30:
        array.append('twenty')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 30 and num < 40:
        array.append('thirty')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 40 and num < 50:
        array.append('forty')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 50 and num < 60:
        array.append('fifty')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 60 and num < 70:
        array.append('sixty')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 70 and num < 80:
        array.append('seventy')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 80 and num < 90:
        array.append('eighty')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    elif num >= 90 and num < 100:
        array.append('ninety')
        ones_digit = get_place(num,0)
        if ones_digit != 0:
            array.append(digit_to_text(ones_digit))
    else: raise ValueError('Number 20 through 99 expected')
    return array

#converts a number less than ten thousand to text
def num_to_text_array(num):
    #redeclares num locally to deal with inputs with preceding zeroes, eg 001
    num = num
    if num == 0:
        return ['zero']
    if num >=10000 or num < 0:
        raise ValueError('Number 0 through 9999 expected')

    s = str(num)
    array = list(s)
    i = len(array) - 1 #ensures compatibility with get_place indexing

    text = []
    while i > 1: #while loop not needed, but reflects organization of subroutines used
        current_digit = get_place(num,i)
        if(current_digit != 0):
            text.append(digit_to_text(current_digit))
            if i == 2:
                text.append('hundred')
            elif i == 3:
                text.append('thousand')
            #######################################################
            #this section can be expanded to express larger numbers
            #######################################################
        i = i - 1

    #retrieves the last two digits of the number
    temp = get_place(num,1)*10 + get_place(num,0)
    tmp_str = ""
    tmp_arr = []

    #this part specific to Project Euler question
    if temp > 0 and num > 100:
        text.append('and')

    if temp > 0 and temp < 10:
        text.append(digit_to_text(temp))
    elif temp >= 10 and temp < 20:
        tmp_str = teen_to_text(temp)
        text.append(tmp_str)
    elif temp >=20 and temp < 100:
        tmp_arr = twenty_to_hundred_to_text(temp)
        for i in range (0,len(tmp_arr)):
            text.append(tmp_arr[i])
    elif temp < 0 or temp > 100:
        raise ValueError('temp value out of bounds')

    return text
