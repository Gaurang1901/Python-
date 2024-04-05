from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

root = Tk()
root.title("Whats Next App")
root.geometry("800x800")
f = ("Times",30,"bold")

l_name = Label(root,text = "Enter Name: ",font = f)
e_name = Entry(root,font = f)
l_name.place(x=30,y=30)
e_name.place(x=320,y=30)

s = IntVar()
s.set(1)
l_sel = Label(root,text = "select any one: ",font = f)
r_job = Radiobutton(root,text = "Job",font = f,variable = s,value = 1)
r_ms = Radiobutton(root,text = "MS",font = f,variable = s,value =2)
r_mba = Radiobutton(root,text = "MBA",font = f,variable = s,value =3)
l_sel.place(x= 30,y = 120)
r_job.place(x=380,y=120)
r_ms.place(x=380,y=148)
r_mba.place(x=380,y=300)

def save():
	con = None
	try:
		con = connect("wn.db")
		cursor = con.cursor()
		sql = "insert into student values('%s','%s')"
		name = e_name.get()
		choice = ""
		if s.get() == 1:
			choice = "job"
		elif s.get() == 2:
			choice == "MS"
		else:
			choice =="MBA"
		cursor.execute(sql %(name,choice))
		con.commit()
		showinfo("save","success")
	except Exception as e:
		showerror("Issue",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		e_name.delete(0,END)
		s.set(1)
		e_name.focus()
		
b_save = Button(root,text = "Save",font = f,command = save)
b_save.place(x=320,y=380)
root.mainloop()
