import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

rt = tkinter.Tk()

#predefine var
intsw = 0
x = 0
num_1 = 0
num_2 = 0
sum_bool = False

vals_store = []

def z(val):
    global vals_store
    global temp
    print(val)
    temp = val
    vals_store.append(val)
    print(vals_store)
    #simple fix slightly sloppy fix later
    try:
        if temp == '*':
            num_1 = ''.join(map(str, vals_store))
            num_1 = int(num_1)
            vals_store.clear()
            sum = temp
            print(num_1)
        elif temp == '/':
            num_1 = ''.join(map(str, vals_store))
            num_1 = int(num_1)
            vals_store.clear()
            sum = temp
            print(num_1)
        elif temp == '+':
            num_1 = ''.join(map(str, vals_store))
            num_1 = int(num_1)
            vals_store.clear()
            sum = temp
            print(num_1)
        elif temp == '-':
            num_1 = ''.join(map(str, vals_store))
            num_1 = int(num_1)
            vals_store.clear()
            sum = temp
            print(num_1)
        else:
            vals_store.append(val)
    except:
        if temp == '*':
            vals_store.pop()
            num_2 = ''.join(map(str, vals_store))
            num_2 = int(num_2)
            print(num_2)
            vals_store.clear()
            sum = temp
        elif temp == '/':
            num_2 = ''.join(map(str, vals_store))
            num_2 = int(num_2)
            vals_store.clear()
            sum = temp
        elif temp == '+':
            num_2 = ''.join(map(str, vals_store))
            num_2 = int(num_2)
            vals_store.clear()
            sum = temp
        elif temp == '-':
            num_2 = ''.join(map(str, vals_store))
            num_2 = int(num_2)
            vals_store.clear()
            sum = temp
        else:
            vals_store.append(val)











one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9'

try:
#screen settings
    rt.title('calculator')
    rt.geometry('200x200')

except:
    showerror('error intalising window')

#buttons
try:
   # for p in range(2):
    tkinter.Button(rt, text="/", font=100,command=lambda: z('/')).grid(column=2, row=4)
    tkinter.Button(rt, text="*", font=100,command=lambda: z('*')).grid(column=1, row=4)
    tkinter.Button(rt, text="0", font=100,command=lambda: z(0)).grid(column=0, row=4)
    tkinter.Button(rt, text="1", font=100,command=lambda: z(1)).grid(column=0, row=3)
    tkinter.Button(rt, text="2", font=100,command=lambda: z(2)).grid(column=1, row=3)
    tkinter.Button(rt, text="3", font=100,command=lambda: z(3)).grid(column=2, row=3)
    tkinter.Button(rt, text="4", font=100,command=lambda: z(4)).grid(column=0, row=2)
    tkinter.Button(rt, text="5", font=100,command=lambda: z(5)).grid(column=1, row=2)
    tkinter.Button(rt, text="6", font=100,command=lambda: z(6)).grid(column=2, row=2)
    tkinter.Button(rt, text="7", font=100,command=lambda: z(7)).grid(column=0, row=1)
    tkinter.Button(rt, text="8", font=100,command=lambda: z(8)).grid(column=1, row=1)
    tkinter.Button(rt, text="9", font=100, command=lambda: z(9)).grid(column=2, row=1)


    tkinter.Label(rt, text=num_1, font=100).grid(column=3, row=1, columnspan=2)
except:
    showerror('Button or label error')
rt.mainloop()




