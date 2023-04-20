# from readline import clear_history
from tkinter import *
def canteen_gui():
    
    # from readline import clear_history
    # from asyncio import exceptions
    # from ast import Global
    from ast import Delete
    from tkinter import messagebox
    from tkinter import filedialog
    from turtle import color
    # from tkinter.tix import COLUMN
    # from turtle import right, width
    # from unittest import result
    from PIL import ImageTk
    from PIL import Image
    from resizeimage import resizeimage
    import webbrowser
    import os,sys
    import win32print
    import win32api
    from tkinter import ttk
    # from tkinter.filedialog
    # import string
    def focus_next_window1(event):
        id_input.tk_focusNext().focus()
        return("break")

    # def focus_next_window2(event):
    #     output.tk_focusNext().focus()
    #     return("break")
    # text_widget=Text(...)
    # text_widget.bind("<Tab>", focus_next_window)

    def handle_ledger():
        student_id=id_input.get()
            # length_id=len(student_id)
        ledger=ledger_input.get()
            # length_ledger=len(ledger)

        if(len(str(student_id))<5 or len(str(student_id))>5):
            messagebox.showerror("Fill all entries","Student ID should consist of 5 digits.")
            return 0
            
        elif(ledger=="" or ledger<'0'):
            messagebox.showerror("Invalid characters","Please input numbers only greater than zero.")
            return 0
            
        elif(student_id[0]=='0' or ledger[0]=='0'):
            messagebox.showerror("Invalid Input","0's in starting is not allowed'")
            return 0
            
            # for i in range(0,len(student_id)):
        if(student_id.isdigit() and ledger.isdigit()):
            return 1
        else:
            messagebox.showerror("Invalid Student ID or Amount","Please input numbers only.")
            return 0
                
    def output_button():
        result= handle_ledger()
        student_id=id_input.get()
        ledger=ledger_input.get()
        if(result):
            messagebox.showinfo("Sucessfull",f"{ledger} ₹ is added as FoodZoned ledger of {student_id}")
        
    def output(event):
        result= handle_ledger()
        student_id=id_input.get()
        ledger=ledger_input.get()
        if(result):
            messagebox.showinfo("Sucessfull",f"{ledger} ₹ is added as FoodZoned ledger of {student_id}")

    def clear_hist():
        # file_to_rem = os.remove("History.txt")
        file_to_rem = open("History.txt", "w")
        file_to_rem.close()
        label1.config(text="")
        
    def history():
        global label1
        with open("History.txt","a") as hist:   
            text=hist.write(f'''Student ID: {id_input.get()} =========>  Amount: {ledger_input.get()}'''"\n")
        with open("History.txt", "r") as content:
            history_text = content.read()
        history_win = Tk()
        history_win.title("History Page")
        history_win.minsize(800,800)
        history_win.configure(bg="black")
        label1 = Label(history_win, text = history_text, fg="#FFD700",bg="black")
        label1.pack()
        histmenu=Menu(history_win)
        histmenu.add_command(label="Print",command=printfile)
        histmenu.add_command(label="Clear History",command=clear_hist)
        history_win.config(menu=histmenu)

    def help():
        msg=messagebox.askquestion("Do you want to contact developer?","Please drop a mail at 'priyansh.sriv03@gmail.com' regarding your problem")
        if(msg=="yes"):
            webbrowser.open("www.Gmail.com")
                
    def printfile():
        # try:
            print_text=filedialog.Open("History.txt")
            win32api.ShellExecute(0,"Print",print_text,None,".", 1 )
        # except exceptions:
        #     print("ERROR")
        #     messagebox.showerror("An Eroor occurred","")
    root=Tk()
    # root.attributes('fullscreen',True)
    root.title("Ledger Entry Page")
    root.iconbitmap("D:\Downloads\Chrome Downloads\PAMS.ico")
    root.geometry("900x900")
    root.minsize(800,500)
    root.configure(background="black")#hexacodes of color
    img1=ImageTk.PhotoImage(Image.open("Ledger_Entery GUI\Canteen Title-canteen title.jpeg"))
    img1.label=Label(root,image=img1)
    img1.label.pack(pady=(0,10),padx=(50,50),fill=BOTH,)
    img1.label.config(borderwidth=0,background="black")
    # resized_img= resizeimage.resize_cover(image=img1,size=[1080,1080])
    # img=ImageTk.PhotoImage(resized_img)
    # text_label=Label(root,text="PSIT FOODZONED",fg="#f9fffb",bg="#770f3f")
    # text_label.config(font=("Rockwell Extra Bold",30))
    # 
    # img=ImageTk.PhotoImage(Image.open("C:\\Users\\priya\\Pictures\\Saved Pictures\\Canteen logo.jpeg"))
    # label used to print text, also can print image.
    # img.label=Label(root,image=img)
    # img.label.pack(pady=(10,10)) #adjusts logo from up and down
    # Pack is used to apply things on gui
    # id_input=IntVar
    # ledger_input=IntVar
    id_label=Label (root,text="Enter Student ID: ",fg="#FFD700",bg="black")
    id_label.pack(pady=(20,5))
    id_label.config(font=('Verdana',30))
    id_input=Entry(root,width=30)
    id_input.pack(pady=4,padx=15)
    id_input.bind("<Return>", focus_next_window1)

    ledger_label=Label(root,text="Enter Amount: ",fg="#FFD700",bg="black")
    ledger_label.pack(pady=(10,5))
    ledger_label.config(font=('Verdana',30))
    ledger_input=Entry(root,width=30)
    ledger_input.pack(pady=4,padx=15)
    ledger_input.bind("<Return>", output)

    # frame2=Frame(root,borderwidth=5, relief=RAISED)
    # frame.pack()
    frame=Frame(root,borderwidth=5, relief=RAISED)
    frame.pack(pady=(20,15))
    add_button= Button(frame,text='Add to Ledger',bg="black",fg="#FFD700",width=20,height=1,command=output_button)
    add_button.config(font=('Verdana',25))
    add_button.pack()
    # add_button.bind("<Return>", output)
    mymenu=Menu(root)
    mymenu.add_command(label="History",command=history)
    mymenu.add_command(label="Help",command=help)
    root.config(menu=mymenu)
    # variable_name=BooleanVar /IntVar
    # checkbox=Checkbutton(text="",variable=)
    # checkbox.pack()
    # root.attributes("-fullscreen",True)
    root.mainloop()