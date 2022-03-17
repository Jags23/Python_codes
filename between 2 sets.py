ar1=[2,4]
ar2=[16,32,96]

maxA=max(ar1)
minB=min(ar2)

cnt=0
for num in range(maxA,minB+1):
    print(num)
    mul=all([num%numA==0 for numA in ar1])
    fact=all([numB%num==0 for numB in ar2])
    cnt=cnt+(mul*fact)

print(cnt)

"""There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1)The elements of the first array are all factors of the integer being considered
2)The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist."""
