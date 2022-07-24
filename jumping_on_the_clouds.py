#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    i=0
    cnt=0
    diff=0
    while True:
        #print(c[i],i)
        if c[i]==1:
            i=i-1
        elif c[i]==0:
            i=i+2
            cnt=cnt+1
            #print("cnt",cnt)
        if i>len(c)-1:
            diff=i-(len(c)-1)
            break

    #print(diff)
    if diff==1:
        return(cnt)
    else:
        return(cnt-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
