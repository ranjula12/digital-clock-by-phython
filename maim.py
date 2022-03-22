from tkinter import*

from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("CLOCK")

def time():
    string = strftime('%I:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)

lable = Label (root, font=("ds-digital",100), background = "black", foreground="red")
lable.pack()
time()

root.mainloop()




