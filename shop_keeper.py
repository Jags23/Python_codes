from collections import Counter
mylist=[]
n=int(input("enter number: "))
for i in range(n):
    mylist.append(int(input()))
    
cnt= Counter(mylist)
print(cnt)
key=list(cnt.keys())
val=list(cnt.values())
total=0
while True:
    cust=input("Enter shoe size: ")
    price=input("enter price ")
    if cust=='Done' and price=='Done':
        print("Total earning today :",total)
        break
    else:
        if cust in key:
       #     print('True')
            ind=key.index(cust)
            val[ind]=val[ind]-1
            if val[ind]<0:
                print("out of stock")
            else :
                total=price+total
            print(key,val,total)
            
        elif cust not in key:
            print("\nShoe size not available today\n")
            
