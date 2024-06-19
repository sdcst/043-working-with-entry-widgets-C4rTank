#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""



import tkinter as tk 

win = tk.Tk()

win.geometry("200x100")

eoutput = tk.StringVar()
eoutput.set("")

def clickFunction(event):
    print(event)
    import math

    a = a_box.get()
    b = a_box.get()
    a = float(a)
    b = float(b)
    a2 = math.pow(a,2)
    b2 = math.pow(b,2)
    c2 = a2 + b2
    c = math.sqrt(c2)
    c = round(c,2)
    answer = str(c)
    answer_entry.insert(2,answer)

a_text = tk.Label(win, text="Enter A")
a_box = tk.Entry(win, width=20)
b_text = tk.Label(win, text="Enter B")
b_box = tk.Entry(win, width=20)

answer_but = tk.Button(win, text="Click Here")

answer_but.bind("<Button>",clickFunction)

answer_label = tk.Label(win, text="C = ")
answer_entry = tk.Entry(win, width=20, textvariable=eoutput)

a_text.grid(row=1,column=1)
b_text.grid(row=2,column=1)
a_box.grid(row=1,column=2)
b_box.grid(row=2,column=2)

answer_but.grid(row=3, column=1, columnspan=2)
answer_label.grid(row=4,column=1)
answer_entry.grid(row=4,column=2)

win.mainloop()

#done