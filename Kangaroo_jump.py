def kang(x1,v1,x2,v2):
    if x1>x2 and v1>v2:
        return 'NO'
    elif x1<x2 and v1<v2:
        return 'NO'
    if v1==v2 and x1!=x2:
        return 'NO'
    if (x2-x1)%(v1-v2)==0 or (x2-x1)%(v2-v1)==0:
        return 'YES'
    else:
        return 'NO'
  
      
print(kang(0,3,4,2))#try with other test cases also
