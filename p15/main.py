#each path has length 2n, and further each path has exactly n steps to the
#right and n steps down. Thus each path corresponds to a word composed of
#the letters as they are specified above, e.g. drddrr for n=3. We can use
#the d's as a partition for the word, and thus we can instead count how many
#r's come between each d.

#for example drrdrd => 0,2,1,0       rrrddd => 3,0,0,0

#the answer to this question is then like placing n unlabeled balls into
#n+1 labeled bins

#the general formula for such a counting is g(m,n) = m+n-1 choose n-1 where
#m is the number of balls and n is the number of bins

#thus for a 20x20 grid, the answer is:
import sys
sys.path.append(r"C:\Users\evans\Google Drive\Code\Python\Project Euler\functions")

from functions import nCr

print(nCr(40,20))
