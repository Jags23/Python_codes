word = input("Enter the word: ")
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

lst=list(d.keys())
lst.sort()
for i in lst:
    print(i, d[i])
