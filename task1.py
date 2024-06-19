"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk 

def run(e):
    data = e1name.get()
    l1name.set(data)
    e2name.set(data)

    data = e1num.get()
    l1num.set(data)
    e2num.set(data)

    data = e1grade.get()
    l1grade.set(data)
    e2grade.set(data)

win = tk.Tk()
win.title("Hello")
win.geometry("500x250")

l1name = tk.StringVar()
e1name = tk.StringVar()
e2name = tk.StringVar()

l1num = tk.StringVar()
e1num = tk.StringVar()
e2num = tk.StringVar()

l1grade = tk.StringVar()
e1grade = tk.StringVar()
e2grade = tk.StringVar()

name = tk.Entry(win,width=16,textvariable=e1name)
name.place(x=200,y=10)
name_text = tk.Label(win,text='Name : ')
name_text.place(x=150,y=8)
name_answer = tk.Label(win, textvariable=l1name)
name_answer.place(x=204,y=177)

num = tk.Entry(win,width=16,textvariable=e1num)
num.place(x=200,y=51)
num_text = tk.Label(win,text='Student Number : ')
num_text.place(x=95,y=48)
num_answer = tk.Label(win, textvariable=l1num)
num_answer.place(x=287,y=199)

grade = tk.Entry(win,width=16,textvariable=e1grade)
grade.place(x=200,y=90)
grade_text = tk.Label(win,text='Student Number : ')
grade_text.place(x=95,y=88)
grade_answer = tk.Label(win, textvariable=l1grade)
grade_answer.place(x=250,y=222)

Enter = tk.Button(win,text="Enter")
Enter.place(x=225,y=125)
Enter.bind("<Button-1>",run)

who = tk.Label(win,text='You are')
what = tk.Label(win,text='Your student number is')
from_ = tk.Label(win,text='You are in Grade')
who.place(x=160,y=175,height=25)
what.place(x=160,y=197,height=25)
from_.place(x=160,y=220,height=25)

win.mainloop()

#done