from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():
	mw.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	mw.deiconify()

def f3():
	mw.withdraw()
	vw.deiconify()
	st_data.delete(1.0,END)
	con=None
	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = "Roll_No: "+str(d[0])+"Name: "+d[1]+"\n"
		st_data.insert(INSERT,info)

	except Exception as e:
		showerror("ISSUE",e)
	finally:
		if con is not None:
			con.close()
def f4():
	vw.withdraw()
	mw.deiconify()

def f5():
	con = None
	try:
		con=connect("kc.db")
		cursor = con.cursor()
		sql = "insert into student values('%d','%s')"
		rno = int(e_rno.get())
		name=e_nme.get()
		cursor.execute(sql % (rno,name))
		con.commit()
		showinfo("SUCCESS","Info Saved")
	except Exception as e:
		showerror("ISSUE",e)
	finally:
		if con is not None:
			con.close()
		e_rno.delete(0,END)
		e_nme.delete(0,END)
		e_rno.focus()

mw = Tk()
mw.title("Student Mgt System")
mw.geometry("700x700")
f=("Times",30,"bold")
#mw.configure(color="cyan")
btn_add=Button(mw,text="Add Student",font=f,width=15,command=f1)
btn_view=Button(mw,text="View Student",font=f,width=15,command=f3)
btn_add.pack(pady=10)
btn_view.pack(pady=10)


aw = Toplevel(mw)
aw.title("Add Student")
aw.geometry("700x700")

l_rno=Label(aw,text="Enter Roll No: ",font=f)
e_rno=Entry(aw,font=f)
l_nme=Label(aw,text="Enter Name: ",font=f)
e_nme=Entry(aw,font=f)
btn_sve=Button(aw,text="Save",font=f,command=f5)
btn_back=Button(aw,text="Back",font=f,command=f2)

l_rno.pack(pady=10)
e_rno.pack(pady=10)
l_nme.pack(pady=10)
e_nme.pack(pady=10)
btn_sve.pack(pady=10)
btn_back.pack(pady=10)
aw.withdraw()

vw = Toplevel(mw)
vw.title("View Student")
vw.geometry("700x700")

st_data = ScrolledText(vw,width=20,height=5,font=f)
vw_btn_back=Button(vw,text="back",font=f,command=f4)
st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

mw.mainloop()
