from tkinter import *
from datetime import *
root = Tk()
root.title("My First App")
root.geometry("800x200+300+200")
root.configure(bg = "cyan")
f=("Verdana",50,"bold","italic")
d = datetime.now().time()
hr = d.hour
if hr<12:
	msg = "Gud Morning"
elif hr<16:
	msg = "Gud Afternoon"
else:
	msg = "Gud Evening"
l = Label(root,text = msg,font = f,fg = "Dark Orange",bg = "cyan")
l.pack(pady=50)
root.mainloop()