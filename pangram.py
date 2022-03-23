def isPan(pangram):
    
    abcd='abcdefghijklmnopqrstuvwxyz'
    strg=''
    #print(pangram)
    lp=[]
    new=[]
    ab=list(abcd)
    for i in pangram:
        lp=list(i)
        for j in lp:
            if j!=' ' and j not in new:
                new.append(j)
            else: continue
        #print(new)
        new.sort()
        if new==list(abcd):
            strg=strg+'1'
            #print(1)
            
        else:
            strg=strg+'0'
            #print(0)
        lp.clear()
        new.clear()

    return strg

pangram=[]
n=int(input("enter a number: "))
print("enter"+str(n)+" strings to check for pangrams")
for i in range(n):
    strn=input()
    pangram.append(strn)
#print(pangram)
result=isPan(pangram)
print(result)
