#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(given):
    # Write your code here
    lst=[]
    new=[]
    newest=[]
    for i in given:
        ind=given.index(i)
        lst.append(ind+1)
    #print(given,lst)

    for j in lst:
        if j in given:
            n=given.index(j)
            new.append(n+1)
        else : continue

    #print(new)

    for a in new:
        if a in given:
            k=given.index(a)
            newest.append(k+1)
    return (newest)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
