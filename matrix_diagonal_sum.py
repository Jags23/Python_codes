arr=[[1,2,3],[4,5,6],[7,8,7]]#any custom square matrix will work
sumr=0      #sum variable for right diagonal
suml=0      #sum variable for left diagonal
for i in range(len(arr)):
    #print(i)
    for j in range(len(arr)):
        #print(arr[i][j])
        if j==i:
            #print(arr[i][j])
            sumr=sumr+arr[i][j]
            
print(sumr)
arr1=[]
for a in range(len(arr)):
    arr[a].reverse()                   #reversing the original matrix 
    #print(arr[a])
    arr1.append(arr[a])

for n in range(len(arr1)):
    #print(i)
    for m in range(len(arr1)):
        #print(arr[i][j])
        if m==n:
            #print(arr1[n][m])
            suml=suml+arr[n][m]
            
print(suml)
diff=sumr-suml
if diff>0:
    print('diff :',diff)
elif diff<0:
    diff=0-diff
    print('diff :',diff)
elif diff==0:
    print('diff :',diff)

    
