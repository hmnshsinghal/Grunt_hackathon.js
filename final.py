#!/bin/python3

import math
import os
import random
import re
import sys


class Movie:
    def __init__(self,Name,Ticket,Cost):
        self.Name= Name
        self.Ticket=Ticket
        self.Cost=Cost
        
    def __str__(self):
        return('Movie : '+str(self.Name) + '\nNumber of Tickets : ' + str(self.Ticket)+ '\nTotal Cost : ' + str(self.Cost))
# Write your code here

if __name__ == '__main__':
    name = input()
    n = int(input().strip())
    cost = int(input().strip())
    
    p1 = Movie(name,n,cost)
    print(p1)

#!/bin/python3

import math
import os
import random
import re
import sys


class comp(object):
    def __init__(self,Real,Imag=0.0):
        self.Real=Real
        self.Imag = Imag
    def add(self, other):
        print('Sum of the two Complex numbers :'+str(self.Real + other.Real)+'+'+str(self.Imag+other.Imag)+'i')
        return complex(self.Real + other.Real,self.Imag + other.Imag)

    def sub(self, other):
        if (self.Imag-other.Imag)<0:
            print('Subtraction of the two Complex numbers :'+str(self.Real - other.Real)+str(self.Imag-other.Imag)+'i')
        else:
            print('Subtraction of the two Complex numbers :'+str(self.Real - other.Real)+'+'+str(self.Imag-other.Imag)+'i')
        return (complex(self.Real - other.Real, self.Imag - other.Imag))
#
#Write your code here

if __name__ == '__main__':
    
    real1 = int(input().strip())
    img1 = int(input().strip())
    
    real2 = int(input().strip())
    img2 = int(input().strip())
    
    p1 = comp(real1,img1)
    p2 = comp(real2,img2)

    p1.add(p2)
    p1.sub(p2)

---------------------------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys



# Write your code here
class rectangle:
    def __init__(self,Length=0,Breadth=0):
        self.Length = Length
        self.Breadth = Breadth
    
    def display(self):
        print('This is a Rectangle')
        #return 
    def area(self,Length=0,Breadth=0):
        print('Area of Rectangle is  '+str(Length * Breadth))
        return(Length * Breadth)
    
class square:
    def __init__(self,side=0):
        self.side=side
    def display(self):
        print('This is a Square')
    def area(self,side=0):
        print('Area of square is  '+str(side**2))
        return (side**2)

if __name__ == '__main__':
    
    l = int(input())
    b = int(input())
    s = int(input())

    obj1 = rectangle()
    obj1.display()
    obj1.area(l,b)

    obj2 = square()
    obj2.display()
    obj2.area(s)

-------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

class parent:
  def __init__(self,total_asset):
    self.total_asset = total_asset

  def display(self):
    print("Total Asset Worth is "+str(self.total_asset)+" Million.")
    print("Share of Parents is "+str(round(self.total_asset/2,2))+" Million.")

# It is expected to create two child classes 'son' & 'daughter' for the above class 'parent'
#
#Write your code here

class son(parent):
    def __init__(self,income, percentage_for_son):
        self.percentage_for_son=percentage_for_son
        self.income=income
    def son_display(self):
        print('Share of Son is '+str(round(self.income*self.percentage_for_son/100,2))+' Million.')
    #parent.display(self,income)
    def display(self):
        print('Total Asset Worth is '+str(self.income)+' Million.')
        print("Share of Parents is "+str(round(self.income/2,2))+" Million.")
    
class daughter(parent):
    def __init__(self,income, percentage_for_daughter):
        self.income=income
        self.percentage_for_daughter=percentage_for_daughter
    def daughter_display(self):
        print('Share of Daughter is '+str(round(self.income*self.percentage_for_daughter/100,2))+' Million.')
    def display(self):
        print('Total Asset Worth is '+str(self.income)+' Million.')
        print("Share of Parents is "+str(round(self.income/2,2))+" Million.")
    

if __name__ == '__main__':

-----------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'Handle_Exc1' function below.
#
#
def Handle_Exc1():
    a=input().split()[0]
    b=input().split()[0]
    #print(a,b)
    if int(a) >= 151 or int(b) <=99 :
        print('Input integers value out of range.')
    elif int(a) + int(b) >= 401:
        print('Their sum is out of range')
    else:
        print('All in range')
   
    # Write your code here
if __name__ == '__main__':
    try:
        Handle_Exc1()
    except ValueError as exp:
        print(exp)
--------------------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys



import itertools
#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#

def performIterator(tuplevalues):
    elist=[]
    alist=[]
    #print(tuplevalues)
    for ele in tuplevalues[0]:
        alist.append(ele)
    elist.append(tuple(alist[:4]))
    elist.append(tuple(itertools.repeat(tuplevalues[1][0],len(tuplevalues[1]))))
    elist.append(tuple(itertools.accumulate(tuplevalues[2])))
    elist.append(tuple(itertools.chain(tuplevalues[0],tuplevalues[1],tuplevalues[2],tuplevalues[3])))
    fftuple=tuple(itertools.chain(tuplevalues[0],tuplevalues[1],tuplevalues[2],tuplevalues[3]))
    elist.append(tuple(itertools.filterfalse(lambda x : x % 2 == 0,fftuple)))
    return tuple(elist)
    # Write your code here

if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)

------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calen' function below.
#
# The function accepts TUPLE datetuple as parameter.
#

def usingcalendar(datetuple):
    # Write your code here
    import calendar
    import datetime
    yy=datetuple[0]
    if yy%4==0:
        mm=2
    else:
        mm=datetuple[1]
        
    dd=datetuple[2]
    # display the calendar
    print(calendar.month(yy, mm))
    obj = calendar.Calendar()
    # iterating with itermonthdates
    lt=[]
    for day in obj.itermonthdates(yy,mm):
        lt.append(day)
    print(lt[-7:])
    
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    
    most = sorted(list(set([datetime.date(yy, mm, 1).weekday() ,datetime.date(yy, mm, calendar.monthrange(yy, mm)[1]).weekday()])))
    if len(most)>1:
        if most[-1]==5:
            print(days[5])
        else :
            print(days[most[0]])
    else:
        print(days[most[0]])
if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)

    usingcalendar(tup)
-------------------------
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
-----------------------------------------------------------------------------
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
        
-----------------------
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
    print(len(List1))
    for i in range(len(List1)):
        print(next(iter1))
        
-------------------------------------------
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
