#!python3
"""
Use the StrinVar.set() method to change the value of a variable to be used
in a Label widget!
"""

import tkinter as tk 


def run(e):
    data = e1Data.get()
    l1Data.set(data)
    e2Data.set(data)
    
win = tk.Tk()

l1Data = tk.StringVar()
e1Data = tk.StringVar()
e2Data = tk.StringVar()

e2IntData = tk.IntVar()

e1 = tk.Entry(win,width=16,textvariable=e1Data)
l1 = tk.Label(win, width=15, textvariable=l1Data)
b1 = tk.Button(win,text="Click for do")
b1.bind("<Button-1>",run)


e1.pack()
l1.pack()
b1.pack()
win.mainloop()