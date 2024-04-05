from tkinter import *
root = Tk()
root.title("My First App")
root.geometry("800x200+300+200")
root.configure(bg = "cyan")
f=("Times new roman",50,"bold","italic")
l = Label(root,text = "Gud Evening",font = f,fg = "red")
l.pack(pady=50)
root.mainloop()