from tkinter import *

root = Tk()
sb = Scrollbar(root)
lb = Text(root, yscrollcommand=sb.set)
for i in range(1000):
    lb.insert(END, str(i))
lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)

mainloop()