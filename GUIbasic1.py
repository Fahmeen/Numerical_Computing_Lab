import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Python GUI')
ttk.Label(win,text="Hello world!!!",).grid(column=1,row=1)
alabel=tk.Label(win,text="againnn",)
alabel.grid(column=0,row=0)
def clickMe():

    action.configure(text="Clicked!")
    alabel.configure(foreground='red')
action=tk.Button(win,text="Click me!",command=clickMe)
action.grid(column=1,row=0)
win.mainloop()
