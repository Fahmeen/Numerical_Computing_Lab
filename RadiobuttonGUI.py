# -*- coding: utf-8 -*-
"""
@author: user
"""

import tkinter as tk
import random
    
win=tk.Tk()
win.title('Languages')
# width x height + x_offset + y_offset:
win.geometry("190x200+30+30") 
     
languages = ['Python','Perl','C++','Java','HTML']
labels = range(5)
for i in range(5):
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = tk.Label(win, 
                text=languages[i], 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)
   l.place(x = 200, y = 100 + i*30, width=125, height=30)
   

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

tk.Label(win, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(win, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
          
win.mainloop()
