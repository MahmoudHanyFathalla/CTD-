import random
from tkinter import *
from PIL import ImageTk, Image

def winn():
  win = Tk()
  win.geometry('700x500')                                                                 
  frame = Frame(win, width=600, height=400)
  frame.pack()
  frame.place(anchor='center', relx=0.5, rely=0.5)
  img = ImageTk.PhotoImage(Image.open('C:\\Users\\hp\\Desktop\\vsc pyy\\koko.PNG'))
  label = Label(frame, image = img)
  label.pack()
  win.mainloop()



def lose():
  w = Tk()
  w.geometry('700x500')                                                                 
  frame = Frame(w, width=600, height=400)
  frame.pack()
  frame.place(anchor='center', relx=0.5, rely=0.5)
  
  img = ImageTk.PhotoImage(Image.open('C:\\Users\\hp\\Desktop\\vsc pyy\\lose.PNG'))
  
  label = Label(frame, image = img)
  label.pack()
  w.mainloop()



lst1=[0,0,0,0,0,0,0,0,0,0]
lst2=[0,0,0,0,0,0,0,0,0,0]
lst3=[0,0,0,0,0,0,0,0,0,0]
lst_user=[]
lst_comp=[]
g=1
check= 5
while(g==1):
  
  print("bag 1    :",lst1)
  print("bag 2    :",lst2)
  print("bag 3    :",lst3)
  print("\t")
  print("your bag :",lst_user)
  print("AI bag   :",lst_comp)
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
           lst_user.append(0)
           check=1
           flag=0
   elif(n==2):
     if (len(lst2) < y or y> 5):
            print("can't remove")
            print("you can't remove more than 5 balls and you can't remove a number which is biger than the bag limit")
            flag=1
     else:
        for i in range(0,y):
           lst2.pop(random.randrange(len(lst2)))
           lst_user.append(0)
           check=1
           flag=0           
   elif(n==3):
     if (len(lst3) < y or y> 5):
            print("can't remove")
            print("you can't remove more than 5 balls and you can't remove a number which is biger than the bag limit")
            flag=1
     else:
        for i in range(0,y):
           lst3.pop(random.randrange(len(lst3)))
           lst_user.append(0)
           check=1
           flag=0
   else:
      print("ERROR : enter a number [1 or 2 or 3]")
      flag=1

  f=1
  while(f==1):
   if(len(lst1)==0 and len(lst2)==0 and len(lst3)==0):
       f=0
   else: 
    k = random. randint(1,3)      
    if(k==1):
        rn=random. randint(1,5)   
        if(len(lst1) < rn):
             f=1
        else:
           for i in range(0,rn):
              lst1.pop(random.randrange(len(lst1)))
              lst_comp.append(0)
              check=0
              f=0
    elif(k==2):
      rn=random. randint(1,5)   
      if(len(lst2) < rn):
             f=1
      else:
          for i in range(0,rn):
             lst2.pop(random.randrange(len(lst2)))
             lst_comp.append(0)
             check=0
             f=0             
    elif(k==3):
       rn=random. randint(1,5)   
       if(len(lst3) < rn):
             f=1
       else:
           for i in range(0,rn):
             lst3.pop(random.randrange(len(lst3)))
             lst_comp.append(0)
             check=0
             f=0             
  if(len(lst1)==0 and len(lst2)==0 and len(lst3)==0):
    g=0
    if(check==0):
        print("YOU WIN")
        fl=0
    else:
        print("YOU LOSE")
        fl=1     
    if(fl==0):
       winn()
    else:
        lose()   











