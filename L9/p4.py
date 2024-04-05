class Employee:
	def __init__(self,id,name,sal):
		self.id = id
		self.name = name	
		self.sal = sal
	def show(self):
		print("ID : ",self.id)
		print("Name : ",self.name)
		print("Salary: ",self.sal)

class SalesPerson(Employee):
	def __init__(self,id,name,sal,comm):
		super().__init__(id,name,sal)	
		self.comm = comm

	def show(self):
		super().show()
		print("Commission : ",self.comm)

s = SalesPerson(10,"Gaurang ",58000,5)
s.show()