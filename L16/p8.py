from tkinter import *
import matplotlib.pyplot as plt

root = Tk()
root.title("Nutrition's Chart")
root.gemoetry("700x700")
f=("Times",25,"bold")

l_name=Label(root,text="Enter Biscuit: ",f)
e_name=Entry(root,f)
l_name.pack(pady=10)
e_name.pack(pady=10)

l_prot=Label(root,"Enter protien qty: ",f)
e_prot=Entry(root,f)
l_prot.pack(pady=10)
e_prot.pack(pady=10)

l_carbs=Label(root,"Enter carbs qty: ",f)
e_carbs=Entry(root,f)
l_carbs.pack(pady=10)
e_carbs.pack(pady=10)

l_fat=Label(root,"Enter fat qty: ",f)
e_fat=Entryt(root,f)
l_fat.pack(pady=10)
e_fat.pack(pady=10)

def gen():
	name=e_name.get()
	prot=float(e_prot.get())
	carbs=float(e_carbs.get())
	fat=float(e_fat.get())
	plt.pie(amt,label=names,autoct)
names=["protien","carbs","fat"]
amt=[prot,"carbs","fat"]
btn_gen=Button(root,text="Generate",command=gen)
btn_gen.pack(pady=30)




root.mainloop()