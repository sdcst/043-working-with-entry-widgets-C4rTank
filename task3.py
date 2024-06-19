#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk


def ADD(event):
    print(event)
    import math

    a = num_box1.get()
    b = num_box2.get()
    a = float(a)
    b = float(b)
    c = a + b
    answer = str(c)
    answer_entry.insert(2,answer)

def SUB(event):
    print(event)
    import math

    a = num_box1.get()
    b = num_box2.get()
    a = float(a)
    b = float(b)
    c = a - b
    answer = str(c)
    answer_entry.insert(2,answer)

def TIME(event):
    print(event)
    import math

    a = num_box1.get()
    b = num_box2.get()
    a = float(a)
    b = float(b)
    c = a * b
    answer = str(c)
    answer_entry.insert(2,answer)

def DIV(event):
    print(event)
    import math

    a = num_box1.get()
    b = num_box2.get()
    a = float(a)
    b = float(b)
    c = a / b
    answer = str(c)
    answer_entry.insert(2,answer)


w = tk.Tk()
w.attributes("-topmost",True)

eoutput = tk.StringVar()
eoutput.set("")

l = []
num_box1 = tk.Entry(w, width=20)
num_box2 = tk.Entry(w, width=20)
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer",state='disabled'))
b=[]
time = tk.Button(w,text="x")
add = tk.Button(w,text="+")
sub = tk.Button(w,text="-")
div = tk.Button(w,text="÷")

add.bind("<Button>",ADD)
sub.bind("<Button>",SUB)
time.bind("<Button>",TIME)
div.bind("<Button>",DIV)

answer_entry = tk.Entry(w, width=20, textvariable=eoutput)

num_box1.grid(row=2,column=1,columnspan=2)
num_box2.grid(row=2,column=3,columnspan=2)
add.grid(row=3,column=1)
sub.grid(row=3,column=2)
time.grid(row=3,column=3)
div.grid(row=3,column=4)

answer_entry.grid(row=4,column=2,columnspan=2)

w.mainloop()

#done