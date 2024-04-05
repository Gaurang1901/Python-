from tkinter import *
import random
import time
def f1():
	clr = ["red","blue","green","yellow","purple","navy blue","cyan","black","brown","grey","pink","salmon"]
	bclr = random.choice(clr)
	root.configure(bg =bclr)
	root.after(2000,f1)
root=Tk()
root.title("Color Me")
root.geometry("600x600+60+60")
f1()
root.mainloop()