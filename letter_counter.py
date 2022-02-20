def most_frequent(string):
    d = dict()
    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1

    lst=list(d.keys())
    
    for i in lst:
        print(i, d[i])
    


word = input("Enter the word: ")
most_frequent(word)
