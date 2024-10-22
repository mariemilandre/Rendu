from tkinter import *
from tkinter import ttk

class Disk:
    def __init__(self, total, used):
        self.total = int(total)
        self.used = int(used)
        self.free = (int(total) - int(used))
        self.used_perc = self.used / self.total * 100

def calculate_used_perc():
        total = totalvar.get()
        used = usedvar.get()
        disk = Disk(total, used)
        usedpercvar.set(disk.used_perc())
        print(disk.used_perc)

root = Tk()

totalvar = StringVar()
usedvar = StringVar()
usedpercvar = StringVar()

#declaration widget
labeltotal = ttk.Label(root, text='Total capacity (Gb)')
entertotal = ttk.Entry(root, textvariable=totalvar)
labelused = ttk.Label(root, text='Used capacity (Gb)')
enterused = ttk.Entry(root, textvariable=usedvar)
percent = ttk.Button(root, text='Percent usage', command=usedpercvar)

#positionnement
percent.grid(row=3, column=1)  
labeltotal.grid(row=1, column=0)
entertotal.grid(row=1, column=1)
labelused.grid(row=2, column=0)
enterused.grid(row=2, column=1)

root.mainloop() 