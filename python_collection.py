#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'collectionfunc' function below.
#
# The function accepts following parameters:
#  1. STRING text1
#  2. DICTIONARY dictionary1
#  3. LIST key1
#  4. LIST val1
#  5. DICTIONARY deduct
#  6. LIST list1
#

def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):
    # Write your code here
    # Write your code here
    #print(text1)
    text1=text1.split()
    wc={words:text1.count(words) for words in sorted(text1)}
    print(wc)
    #fdt={key:dictionary1[key]-deduct[key] for key in deduct}
    #for key in fdt:
        #dictionary1[key]=fdt[key]
    for key in deduct:
        if key not in dictionary1:
            dictionary1[key]=-deduct[key]
        else:
            dictionary1[key]=dictionary1[key]-deduct[key]
    print(dictionary1)
    #print(deduct)
    #print(dictionary1)
    mapdt={key1[i]:val1[i] for i in range(len(key1))}
    del mapdt[key1[1]]
    mapdt[key1[1]]=val1[1]
    print(mapdt)
    #print(val1)
    #print(deduct)
    dt2={'odd':[],'even':[]}
    for ele in list1:
        if ele%2==0:
            dt2['even'].append(ele)
        else :        
            dt2['odd'].append(ele)
    if len(dt2['odd'])==0:
        del dt2['odd']
    if len(dt2['even'])==0:
        del dt2['even']
    print(dt2)
if __name__ == '__main__':
    from collections import Counter

    text1 = input()
    
    n1 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n1):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict={}
    for i in range(n1):
        testdict[qw1[i]]=qw2[i]
    collection1 = (testdict)
    
    qw1 = []
    n2 = int(input().strip())
    for _ in range(n2):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
    key1 = qw1
    
    qw1 = []
    n3 = int(input().strip())
    for _ in range(n3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    val1 = qw1

    n4 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n4):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict={}
    for i in range(n4):
        testdict[qw1[i]]=qw2[i]
    deduct = testdict

    qw1 = []
    n5 = int(input().strip())
    for _ in range(n5):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    list1 = qw1

    collectionfunc(text1, collection1, key1, val1, deduct, list1)
