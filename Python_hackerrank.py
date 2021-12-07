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
        print('Area of Rectangle is '+str(Length * Breadth))
        return(Length * Breadth)
    
class square:
    def __init__(self,side=0):
        self.side=side
    def display(self):
        print('This is a Square')
    def area(self,side=0):
        print('Area of square is '+str(side**2))
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
        print('Total Asset Worth is '+str(self.income)+' Million')
        print("Share of Parents is "+str(round(self.income/2,2))+" Million.")
    
class daughter(parent):
    def __init__(self,income, percentage_for_daughter):
        self.income=income
        self.percentage_for_daughter=percentage_for_daughter
    def daughter_display(self):
        print('Share of Son is '+str(round(self.income*self.percentage_for_daughter/100,2))+' Million ')
    def display(self):
        print('Total Asset Worth is '+str(self.income)+' Million')
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
