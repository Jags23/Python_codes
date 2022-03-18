import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(lst):
    # Write your code here
    d = dict()
    for c in lst:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1

    #print(d)
    #print("keys-->",d.keys())
    #print("Values-->",d.values())
    val=list(d.values())
    k=list(d.keys())
    ind=val.index(max(val))
    mini=k[ind]
    #print("Mini",mini)
    for i in range(len(val)):
        if val[i]==max(val):
            #print(val[i],k[i])
            if k[i]<mini:
                mini=k[i]

    return mini

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
