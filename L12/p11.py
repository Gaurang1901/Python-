from tkinter import *
def f1():
	root.configure(bg = "red")
def f2():
	root.configure(bg = "blue")
def f3():
	root.configure(bg = "green")
root=Tk()
root.title("Color Me")
root.geometry("600x600+60+60")
f = ("Times",30,"bold")
btn_red = Button(root,text="Red",font=f,bg = "light blue",fg = "black",command = f1)
btn_blue = Button(root,text="blue",font=f,bg = "light blue",fg = "black",command = f2)
btn_green = Button(root,text="green",font=f,bg = "light blue",fg = "black",command = f3)
btn_red.pack(pady = 20)
btn_blue.pack(pady = 20)
btn_green.pack(pady = 20)
root.mainloop()