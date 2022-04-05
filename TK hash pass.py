from tkinter import *
import hashlib
global txt
global username
global password
def regist():

    right_user = "mahmoud"
    right_pass = "tmsaa7"
    right_user_h = hashlib.md5(right_user.encode('utf_8')).hexdigest()
    right_pass_h = hashlib.md5(right_pass.encode('utf_8')).hexdigest()
    user=username.get()
    pas=password.get()
    user_h = hashlib.md5(user.encode('utf_8')).hexdigest()
    pass_h = hashlib.md5(pas.encode('utf_8')).hexdigest()
    if(user=='' or pas==''):
       txt.set("please enter your name and pass")
    elif(user_h == right_user_h and pass_h == right_pass_h):
       txt.set("WELLCOM")
    else:
       txt.set("Wronng pass or Wronng user name")

            
screan   = Tk()
username = StringVar()
password = StringVar()
txt      = StringVar()
screan.title("Login page")
screan.geometry("550x300")
screan.configure(bg='black')    
txt.set("ENTER YOUR NAME AND PASSWORD")
Label(screan, text="Name :",bg="red").place(x=20,y=40)
Label(screan, text="Pass : ",bg="red").place(x=20,y=100)
Entry(screan,width = "60",textvariable=username).place(x=100,y=42)
Entry(screan, width="60" ,textvariable=password ,show="#").place(x=100,y=100)
Label(screan,textvariable=txt).place(x=160,y=150)
Button(screan, text="Login", width=30, height=2, bg="red",command=regist).place(x=150,y=200)
screan.mainloop()
