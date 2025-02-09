import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

rt = tkinter.Tk()

try:
    #geting screen size
    sw = str(rt.winfo_screenwidth())
    sh = str(rt.winfo_screenheight())
    screen = sw + 'x' + sh

    #
    rt.title('calculator')
    rt.geometry(screen)
    rt.mainloop()
except:
    showerror('error intalising window')


