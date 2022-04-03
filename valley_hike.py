path=input()
ar=list(path)
print(ar)
sum1=0

count=0
for i in ar:
    if i =='U':
        sum1=sum1+1
        
    elif i=='D':
        sum1=sum1-1
    #print(i,sum1)
    if i=='U' and sum1==0:
        count=count+1
print(count)
    
