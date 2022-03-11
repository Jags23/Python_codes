def timeConversion(s):
    # Write your code here
    sc=':'
    h=int(s[:2])
    m=str(s[3:5])
    sec=str(s[6:8])
    #print(h,m,sec)
    time=s[8:]
    if time=='AM':
        if h==12:
            h='00'
        elif h!=12:
            h=str(s[:2])
    elif time=='PM':
        if h!=12:
            h=h+12

    #print(h,m,sec)
    #print(s)
    return (str(h)+sc+str(m)+sc+str(sec))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
