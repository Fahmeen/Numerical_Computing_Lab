# -*- coding: utf-8 -*-
"""
@author: user
"""

import tkinter as tk
import random
    
win=tk.Tk()
win.title('Languages')
# width x height + x_offset + y_offset:
win.geometry("170x200+30+30") 
     
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
   l.place(x = 20, y = 30 + i*30, width=125, height=30)
          
win.mainloop()