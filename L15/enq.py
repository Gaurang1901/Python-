from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from pymongo import*
from datetime import*

root = Tk()
root.title("Kamal classes")
root.geometry("700x700+20+20")
f = ("Simsun",30,"bold")
lab_enquiry = Label(root,text = "Enquiry Form is here...",font=f)
lab_enquiry.pack(pady=20)

lab_name = Label(root,text = "Enter name ",font=f)
ent_name = Entry(root, font=f)
lab_name.pack()
ent_name.pack()

lab_phone = Label(root,text = "Enter phone ",font=f)
ent_phone = Entry(root, font=f)
lab_phone.pack()
ent_phone.pack()

lab_query = Label(root,text = "Enter query ",font=f)
st_query = ScrolledText(root,width =20,height=4, font=f)
lab_query.pack()
st_query.pack()

def save():
	con = None
	try:
		con = MongoClient("localhost",27017)
		db = con["enq"]
		coll = db["students"]
		name = ent_name.get()
		phone = ent_phone.get()
		query = st_query.get(0.0,END)
		dt = datetime.now()
		info = {"name":name,"phone":phone,"query":query,"enddt":dt}
		coll.insert_one(info)
		showinfo("Success","We will get back to you")
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
		ent_name.delete(0,END)
		ent_phone.delete(0,END)
		st_query.delete(1.0,END)
		ent_name.focus()

btn_submit = Button(root, text="Submit",font=f, command=save)
btn_submit.pack(pady=20)

root.mainloop()