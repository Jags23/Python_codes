from collections import Counter

def checkMagazine(mag, note):
    # Write your code here
    d=Counter(mag)
    cnt=True
    for i in note :
        if i in d and d[i]>=0:
            d[i]=d[i]-1
            if d[i]<0:
                cnt=False
                break
        if i not in d:
            cnt=False
            break
        #print(d)
    if cnt==True:
        print('Yes')
    elif cnt==False:
        print('No')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
