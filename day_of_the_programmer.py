def dayOfProgrammer(yr):
    # Write your code here
    Leap=False
    if yr%100==0 and yr%400==0:
        #print('Leap')
        Leap=True
    elif yr%4==0 and yr%100!=0:
        #print('Leap')
        Leap=True
    else:
        #print("Not leap")
        Leap=False
    if yr>1918 and Leap==True:
        return ("12.09."+str(yr))
    elif yr>1918 and Leap==False:
        return ("13.09."+str(yr))
    if yr==1918:
        return ("26.09.1918")
    if yr<1918 and yr>=1700 and yr%4==0:
        return ("12.09."+str(yr))
    elif yr<1918 and yr>=1700 and yr%4!=0:
        return ("13.09."+str(yr))
      
 
year=int(input('Enter a year: '))
print(dayOfProgrammer(year))
