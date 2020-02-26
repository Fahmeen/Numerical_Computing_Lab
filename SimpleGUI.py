import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Python GUI')
ttk.Label(win,text="Introduction to python..",).grid(column=1,row=1)
ttk.Label(win,text="Numerical Computing..",).grid(column=0,row=0)
win.mainloop()
