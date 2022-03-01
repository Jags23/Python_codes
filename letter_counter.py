def most_frequent(string):
    d = dict()
    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1                # d stores the letters available in the word, with their respective count(unsorted)

    lst=sorted(d.items(), key=lambda x:x[1], reverse=True) # lst stores the the dict as a 2d list which is sorted by value
    d1=dict(lst)                        #d1 is a dict made up of lst
    lst1=list(d1.keys())                 #lst1 only has the key values of d1
    for i in lst1:
        print(i, d1[i])
    


word = input("Enter the word: ")
most_frequent(word)
