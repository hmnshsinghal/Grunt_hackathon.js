#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'FORLoop' function below.
#

def FORLoop():
    # Write your code here
    n=input().split()
    List1=[]
    #print(n[0])
    for i in range(0,int(n[0])):
        a=input().split()
        List1.append(int(a[0]))
    #print(input().split())
    print(List1)
    iter1=iter(List1)
    #print(len(List1))
    for i in range(len(List1)):
        print(next(iter1))
    return iter1

if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))
  
    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')
