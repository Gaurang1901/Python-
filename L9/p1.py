class person:
	def __init__(self,id,name,add):
		self.id = id
		self.name = name
		self.add = add
	def display(self):
		print("\nID : ",self.id)
		print("Name : ",self.name)
		print("Address : ",self.add)

p1 = person(10,"Gaurang","Kalwa")
p1.display()

p2 = person(20,"Yadnesh","Thane")
p2.display()