# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 22:40:51 2022

@author: JAGADEEP T
"""

import csv

def write_to_file(lst):
    with open('info1.csv','a') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(['Name','Age','Contact','Email'])
            
        writer.writerow(lst)

if __name__=='__main__':

    count=1
    cond=True
    while (cond):
        info=input('Enter student #{} information in the specified format--> (Name age contact email) :'.format(count))
        print(info)
        lst=info.split(' ')
        print(lst)
        print("\nEntered information is -\nName:{}\nAge:{}\nContact number:{}\nEmail:{}".format(lst[0],lst[1],lst[2],lst[3]))
        correct=input("Do you like to enter this information? :(Y/N)")
        if correct=='Y':
             write_to_file(lst)
             cont=input('Proceed to enter information of other students? (Y/N)')
             count=count+1
             if cont=='Y':
                cond=True
             elif cont=='N':
                cond=False
                
        elif correct=='N':
            print("\nPlease enter the correct information")
            

