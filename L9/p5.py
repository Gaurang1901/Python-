class person:
	def __init__(self,id,name,add):
		self.id = id
		self.name = name
		self.add = add
	def show(self):
		print("\nId : ",self.id)
		print("Name : ",self.name)
		print("Address : ",self.add)

class Teacher(person):
	def __init__(self,id,name,add,sal):
		super().__init__(id,name,add)
		self.sal = sal
	def show(self):
		super().show()
		print("Salary: ",self.sal)

class Hod(Teacher):
	def __init__(self,id,name,add,sal,dept):
		super().__init__(id,name,add,sal)
		self.dept = dept
	def show(self):
		super().show()
		print("Department: ",self.dept)

p = person(10,"Gaurang","Kalwa")
p.show()

t = Teacher(20,"Yadnesh","Thane",25000)
t.show()

h = Hod(30,"RedX","Thane",30000,"CO")
h.show()