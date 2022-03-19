def bonAppetit(bill, k, b):
    # Write your code here
    sum1=0
    for i in range(len(bill)):
        if i==k:
            continue
        else:
            sum1=sum1+bill[i]
    if b==int(sum1/2):
        print("Bon Appetit")
    else:
        print(b-int((sum1/2)))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
