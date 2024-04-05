from tkinter import *
import random
import time
def f1():
	while True:
		clr = ["red","blue","green","yellow","purple","navy blue","cyan","black","brown","grey","pink","salmon"]
		bclr = random.choice(clr)
		root.configure(bg =bclr)
		time.sleep(5)
root=Tk()
root.title("Color Me")
root.geometry("600x600+60+60")
#f = ("Times",30,"bold")
#btn_clr= Button(root,text="Color",font=f,bg = "light blue",fg = "black",command = f1)
#btn_clr.pack(pady = 20)
f1()
root.mainloop()