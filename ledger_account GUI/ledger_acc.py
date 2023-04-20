from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, width
from PIL import Image
from PIL import ImageTk
import datetime

def generate_token():
    # time=clock()
    global count
    time=datetime.datetime.now().strftime("%H:%M:%S")
    clock=datetime.datetime.now().time()
    if (clock.hour == 0 and clock.minute == 0):
        count=1

    else:
        count+=1
    
    messagebox.showinfo("Token Number",f"Your token numer is: {count}\nTime: {time}\n Valid for:- 2 hours")

    

    
    
# def clock():
#     time=datetime.datetime.now().strftime("%H:%M:%S")
#     return time


root=Tk()
root.title("Token Generator")
# root.iconbitmap("")
root.geometry("400x300")
root.configure(background="white")
root.minsize(300,300)
# root.maxsize(300,200)

# Food menu.grid
menu1=Label(root,text="Samosa",bg="white").grid(row=0,column=0)
menu2=Label(root,text="Ice Cream",bg="white").grid(row=1,column=0)
menu3=Label(root,text="Chips",bg="white").grid(row=2,column=0)
menu4=Label(root,text="Cold Drink",bg="white").grid(row=3,column=0)
menu5=Label(root,text="Chole Bhature",bg="white").grid(row=4,column=0)
menu6=Label(root,text="Water",bg="white").grid(row=5,column=0)
menu7=Label(root,text="Chowmein",bg="white").grid(row=0,column=49)
menu8=Label(root,text="Fried rice",bg="white").grid(row=1,column=49)
menu9=Label(root,text="Patiees",bg="white").grid(row=2,column=49)
menu10=Label(root,text="Paneer Wrap",bg="white").grid(row=3,column=49)
menu11=Label(root,text="Aalu Wrap",bg="white").grid(row=4,column=49)
menu12=Label(root,text="Biryani",bg="white").grid(row=5,column=49)

#check button
b1=IntVar
#check Button
check=Checkbutton().grid(row=0,column=1)
check=Checkbutton().grid(row=1,column=1)
check=Checkbutton().grid(row=2,column=1)
check=Checkbutton().grid(row=3,column=1)
check=Checkbutton().grid(row=4,column=1)
check=Checkbutton().grid(row=5,column=1)
check=Checkbutton().grid(row=0,column=50)
check=Checkbutton().grid(row=1,column=50)
check=Checkbutton().grid(row=2,column=50)
check=Checkbutton().grid(row=3,column=50)
check=Checkbutton().grid(row=4,column=50)
check=Checkbutton().grid(row=5,column=50)

#Token Button
frame=Frame(root,borderwidth=5, relief=RAISED)
frame.grid(row=7,column=20,pady=(20,15))
token_button=Button(frame,text="Generate Token",bg="red",fg="white",command=generate_token)
token_button.grid(row=7,column=20)




count = 0
root.mainloop()