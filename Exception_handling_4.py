#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Library' function below.
#

 
def Library(memberfee,installment,book):
    # Write your code here
    if installment >3 :
        #print('the input for the number of installments is greater than 3')
        print('Maximum Permitted Number of Installments is 3')
    elif installment == 0:
        print('Number of Installments cannot be Zero.')
    else :
        amount = memberfee / installment
        print('Amount per Installment is  '+ str(amount))    
        #Amount per Installment is  3000.0
        book_section = ['philosophers stone','chamber of secrets','prisoner of azkaban','goblet of fire','order of phoenix','half blood prince','deathly hallows 1','deathly hallows 2']
        if book in book_section :
            print('It is available in this section')
        else :
            print('No such book exists in this section')
    #print(memberfee,installment,book)
    #if book in book_section :
        #print('It is available in this section')
    #else :
        #print('No such book exists in this section')
        

    #It is available in this section

if __name__ == '__main__':
    
    memberfee = int(input())
    installment = int(input())
    book = input()
    
    try:
        Library(memberfee,installment,book)
        
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)
