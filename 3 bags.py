
import random
from tkinter import *
from PIL import ImageTk, Image
import cv2


lst1=[0,0,0,0,0,0,0,0,0,0]
lst2=[0,0,0,0,0,0,0,0,0,0]
lst3=[0,0,0,0,0,0,0,0,0,0]

g=1
check= 5

while(g==1):
  ai=0
  o=0
  p=0
  pp=0
  ppp=0
  j=0
  v=0
  print("bag 1    :",lst1)
  print("bag 2    :",lst2)
  print("bag 3    :",lst3)
  print("\t")
  
  flag=1
  while(flag==1):
   while True:
    try:
        n = int(input("Enter number of bag [1 or 2 or 3] : "))
        y = int(input("Enter number of elements you want to take : "))
        break
    except ValueError:
          print("Oops!  That was no valid number.  Try again...")
       
   if(n==1):
     if (len(lst1) < y or y> 5):
            print("can't remove")
            print("you can't remove more than 5 balls and you can't remove a number which is biger than the bag limit")
            flag=1
     else:
        for i in range(0,y):
           lst1.pop(random.randrange(len(lst1)))
           check=1
           flag=0
           ai=1
        print(f"u pop {y} balls from bag 1")   
   elif(n==2):
     if (len(lst2) < y or y> 5):
            print("can't remove")
            print("you can't remove more than 5 balls and you can't remove a number which is biger than the bag limit")
            flag=1
     else:
        for i in range(0,y):
           lst2.pop(random.randrange(len(lst2)))
           check=1
           flag=0
           ai=2           
        print(f"u pop {y} balls from bag 2 ")   
   elif(n==3):
     if (len(lst3) < y or y> 5):
            print("can't remove")
            print("you can't remove more than 5 balls and you can't remove a number which is biger than the bag limit")
            flag=1
     else:
        for i in range(0,y):
           lst3.pop(random.randrange(len(lst3)))
           check=1
           flag=0
           ai=3
        print(f"u pop {y} balls from bag 3 ")   
   else:
      print("ERROR : enter a number [1 or 2 or 3]")
      flag=1

      
  while (True):
   if(len(lst1)==0 and len(lst2)==0 and len(lst3)==0):
     break 
   if(ai==1):
    if(len(lst1)<=5 and len(lst1)!=0):
      v=len(lst1)
      for i in range(0,len(lst1)):
           lst1.pop(random.randrange(len(lst1)))
      print(f"computer pops {v} balls from bag 1 ")
      check=0
      break     
    elif(len(lst1)==7):
           lst1.pop(random.randrange(len(lst1)))
           print(f"computer pops 1 ball from bag 1 ")
           check=0
           break  
    elif(len(lst1)==8):
      for i in range(0,2):
           lst1.pop(random.randrange(len(lst1)))
      print(f"computer pops 2 balls from bag 1 ")
      check=0
      break       
    elif(len(lst1)==9):
      for i in range(0,3):
           lst1.pop(random.randrange(len(lst1)))
      print(f"computer pops 3 balls from bag 1 ")
      check=0
      break       
    elif(len(lst1)==10):
      for i in range(0,4):
           lst1.pop(random.randrange(len(lst1)))
      print(f"computer pops 4 balls from bag 1 ")
      check=0
      break
    elif(len(lst1)==0):
      ai=2       
      o=1
    elif(len(lst1)==6 and len(lst2)==0 and len(lst3)==0):
      lst1.pop(random.randrange(len(lst1)))
      print(f"computer pops 1 ball from bag 1 ")
      check=0
      break
    elif(len(lst1)==6 and j !=1):
      ai=2
      p=1   
    elif(j==1):
      lst1.pop(random.randrange(len(lst1)))
      print(f"computer pops 1 ball from bag 1 ")
      j=0
      break
    check=0       
   if(ai==2):
    if(len(lst2)<=5 and len(lst2)!=0):
      b=len(lst2)
      for i in range(0,len(lst2)):
           lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops {b} balls from bag 2 ")
      check=0   
      break       
    elif(len(lst2)==7):
           lst2.pop(random.randrange(len(lst2)))
           print(f"computer pops 1 ball from bag 2 ")
           check=0
           break  
    elif(len(lst2)==8):
      for i in range(0,2):
           lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops 2 balls from bag 2 ")
      check=0
      break     
    elif(len(lst2)==9):
      for i in range(0,3):
           lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops 3 balls from bag 2 ")
      check=0
      break     
    elif(len(lst2)==10):
      for i in range(0,4):
           lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops 4 balls from bag 2 ")
      check=0
      break
    elif(v==1):
      lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops 1 ball from bag 2 ")
      check=0
      break
    elif(len(lst2)==0):
      ai=3
      o=2  
    elif(len(lst2)==6 and len(lst1)==0 and len(lst3)==0):
      lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops 1 ball from bag 2 ")
      check=0
      break  
    elif(len(lst2)==6):
      ai=3 
      pp=1 
    elif(j==1):
      lst2.pop(random.randrange(len(lst2)))
      print(f"computer pops 1 ball from bag 2 ")
      j=0      
      break 
    check=0       
   if(ai==3):
    if(len(lst3)<=5 and len(lst3)!=0):
      n=len(lst3)
      for i in range(0,len(lst3)):
           lst3.pop(random.randrange(len(lst3)))
      print(f"computer pops {n} balls from bag 3 ")
      check=0
      break     
    elif(len(lst3)==7):
           lst3.pop(random.randrange(len(lst3)))
           print(f"computer pops 1 ball from bag 3 ")
           check=0
           break
    elif(len(lst3)==8):
      for i in range(0,2):
           lst3.pop(random.randrange(len(lst3)))
      print(f"computer pops 2 balls from bag 3 ")
      check=0
      break     
    elif(len(lst3)==9):
      for i in range(0,3):
           lst3.pop(random.randrange(len(lst3)))
      print(f"computer pops 3 balls from bag 3 ") 
      check=0 
      break   
    elif(len(lst3)==10):
      for i in range(0,4):
           lst3.pop(random.randrange(len(lst3)))
      print(f"computer pops 4 balls from bag 3 ")
      check=0
      break
    elif(v==3):
      lst3.pop(random.randrange(len(lst3)))
      print(f"computer pops 1 balls from bag 3 ") 
      check=0 
      break 
    elif(len(lst3)==0):
      ai=1
      o=3  
    elif(len(lst3)==6):
      ai=1       
      ppp=1
    elif(j==1):
      lst3.pop(random.randrange(len(lst3)))
      print(f"computer pops 1 ball from bag 3 ")
      j=0  
      break
    check=0
   if(pp==1 and p==1 and ppp==1):
      j=1
      ai=1
   if(o==1 and pp==1 and ppp==1):
     v=1   
     ai=2
   if(o==2 and ppp==1):
     v=3 
     ai=3
   
  if(len(lst1)==0 and len(lst2)==0 and len(lst3)==0):
    
    if(check==0):
        img = cv2.imread('C:\\Users\\hp\\Desktop\\vsc pyy\\lose.PNG', 1)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("you lose")
    else:
        img = cv2.imread('C:\\Users\\hp\\Desktop\\vsc pyy\\koko.PNG',1)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        print("you win")    
 
