#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Bank_ATM' function below.
#
# Define the Class for user-defined exceptions "MinimumDepositError" and "MinimumBalanceError" here






def Bank_ATM(balance,choice,amount):
    # Write your code here
    #print(balance,choice,amount)
    if balance < 500:
        print('As per the Minimum Balance Policy, Balance must be at least 500')
    elif choice == 1:
        if amount < 2000:
            print('The Minimum amount of Deposit should be 2000.')
        else :
            balance = balance +amount
            print('Updated Balance Amount:  '+ str(balance))
    else :
        #print(balance,amount)
        balance = balance - amount
        #print(balance,amount)
        if balance <500:
            print('You cannot withdraw this amount due to Minimum Balance Policy')
        else :            
            #print(balance,amount)
            print('Updated Balance Amount:  '+ str(balance))
#Updated Balance Amount:  2000
if __name__ == '__main__':
    
    bal = int(input())
    ch = int(input())
    amt = int(input())
    
    try:
        Bank_ATM(bal,ch,amt)
    
    
    except ValueError as e:
        print(e)
    except MinimumDepositError as e:
        print(e)
    except MinimumBalanceError as e:
        print(e)
