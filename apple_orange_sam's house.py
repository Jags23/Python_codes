def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    da=s-a#pos
    db=t-b#neg
    ac=0
    oc=0
    for apple in apples:
        if apple<0:
            continue
        elif apple>=da and apple<=(t-a):
            ac=ac+1
    for orange in oranges:
        if orange>0:
            continue
        elif orange<=db and orange>=(s-b):
            oc=oc+1
            
    print(ac)
    print(oc)     
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
