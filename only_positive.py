n=int(input('Number of terms in list :'))
list1=[]
print('\nEnter the values:\n')
for i in range(n):
    num=int(input())
    list1.append(num)

print('Input list: ',list1)
list2=[]
for j in list1:
    if j>=0:
        list2.append(j)

print("Output list: ",list2)


#I took inputs for the list1 from user and then included them in the list1 using .append function
