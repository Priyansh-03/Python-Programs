import mysql.connector as ms
from tkinter import *
from pathlib import Path
from LedgerEntry_GUI import canteen_gui

cn=ms.connect(host="localhost",user="root",passwd="hacker",database="test")
if cn.is_connected():
    print("Successfully connected :)")

else:
    print("ERROR")

cr=cn.cursor()

cr.execute("show databases")

for i in cr:
    print(i)

gui=canteen_gui()