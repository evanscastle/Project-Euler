import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from local_methods import get_tri_between, get_hex_between, get_pent_between

#step size of lists to be generate
CONST = 100000
NUM_MATCHES = 3


final = []

i = 0
#loop checks numbers 100000 at a time to avoid extra computational waste
while len(final) < NUM_MATCHES:
    #records numbers which are both triangular and pentagonal
    tri_and_hex = []
    #records numbers which are both pentagonal and hexagonal
    pent_and_hex = []

    #range grows quadratically to reflect the growth of the numbers
    tri = get_tri_between(CONST*i**2, CONST*(i+1)**2)
    pent = get_pent_between(CONST*i**2, CONST*(i+1)**2)
    hex = get_hex_between(CONST*i**2, CONST*(i+1)**2)

    #We compare both lists to hex because hex is the shortest list. We then compare
    #the resulting lists to one another
    for j in range(0, len(hex)):
        if hex[j] in tri:
            tri_and_hex.append(hex[j])

    for j in range(0, len(hex)):
        if hex[j] in pent:
            pent_and_hex.append(hex[j])

    #This iterative search cuts down on the cost of additional searches since
    #we are only interested in elements that are members of all three sets
    for j in range(0, len(pent_and_hex)):
        if pent_and_hex[j] in tri_and_hex:
            final.append(pent_and_hex[j])

    i += 1

print(final)
