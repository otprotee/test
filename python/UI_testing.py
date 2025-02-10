import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

rt = tkinter.Tk()

#predefine var
sw = 0
sh = 0
intsw = 0
x = 0

vals_store = []

def z(val):
    global vals_store
    vals_store.append(val)
    print(vals_store)



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
    #getting screen size
    sw = str(rt.winfo_screenwidth())
    sh = str(rt.winfo_screenheight())
    screen = sw + 'x' + sh

    #screen settings
    rt.title('calculator')
    rt.geometry(screen)

except:
    showerror('error intalising window')

#buttons
intsw = int(sw)
bw = intsw/4

tkinter.Button(rt, text="0", command=lambda: z(0)).grid(column=0, row=5)
tkinter.Button(rt, text="1", command=lambda: z(1)).grid(column=0, row=4)
tkinter.Button(rt, text="2", command=lambda: z(2)).grid(column=1, row=4)
tkinter.Button(rt, text="3", command=lambda: z(3)).grid(column=2, row=3)
tkinter.Button(rt, text="4", command=lambda: z(4)).grid(column=0, row=3)
tkinter.Button(rt, text="5", command=lambda: z(5)).grid(column=1, row=3)
tkinter.Button(rt, text="6", command=lambda: z(6)).grid(column=2, row=2)
tkinter.Button(rt, text="7", command=lambda: z(7)).grid(column=0, row=2)
tkinter.Button(rt, text="8", command=lambda: z(8)).grid(column=1, row=2)
tkinter.Button(rt, text="9", command=lambda: z(9)).grid(column=2, row=1)

rt.mainloop()




