n1=0
n2=1
count=1
terms=int(input('Enter the number of terms(including initial terms) :'))
print('initial terms:0,1')
while (terms-1)>count:
    new=n1+n2
    print(new)
    n1=n2
    n2=new
    count=count+1
print('Done')

#this program intends to print fibonacci series
