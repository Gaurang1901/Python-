from tkinter import *
from sqlite3 import *
from tkniter.messagebox import *

root = Tk()
root.title("Success Stories")
root.geometry("600x800")
f = ("Times",30,"bold")

l_nme = Label(root,text = "Enter Name: ",font = f)
e_nme = Entry(root,font = f)
l_nme.pack(pady = 10)

l_comp = Label(root,text = "Enter Company: ",font = f)
e_comp = Entry(root,font = f)
l_comp.pack(pady = 10)

l_pkg = Label(root,text = "Enter Package: ",font = f)
e_pkg = Entry(root,font = f)
l_pkg.pack(pady = 10)

def save():
	con = None
	try:
		con = connect("ss.db")
		cursor = con.cursor()
		sql = "insert into student values('%s','%s','%d')"
		name = e_nme.get()
		comp = e_comp.get()
		pkg = float(e_pkg.get())
		cursor.execute(sql %(name,comp,pkg))
		con.commit()
		showinfo("Success","Saved")
	except Exception as e:
		con.rollback()
		showerror("Issue",str(e))
	finally:
		if con is not None:
			con.close()
		e_nme.delete(0,END)
		e_comp.delete(0,END)
		e_pkg.delete(0,END)
		e_nme.focus()

btn_sve = Button(root,text = "Save",font = f,command = save)
btn_sve.pack(pady = 10)
root.mainloop()