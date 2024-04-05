class person:
	def __init__(self,id,name,loc,phn):
		self.id = id
		self.name = name
		self.loc = loc		
		self.phn = phn
	def show(self):
		print("ID : ",self.id)
		print("Name : ",self.name)
		print("Location : ",self.loc)
		print("Phone No: ",self.phn)

class student(person):
	def __init__(self,id,name,loc,phn,mrks):
		super().__init__(id,name,loc,phn)	
		self.mrks = mrks

	def show(self):
		super().show()
		print("marks : ",self.mrks)

s = student(10,"amit ","thane",999,85)
s.show()