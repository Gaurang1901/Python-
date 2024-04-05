class Person:
	def __init__(self,name,add):
		self.id = id
		self.name = name
		self.add = add
	def display(self):
		print("Name : ",self.name)
		print("Address : ",self.add)

data = {}

while True:
	op = int(input("1: New \n2: View \n3: Delete \n4:Exit\n"))
	if op ==1:
		id = int(input("Enter Id: "))
		if data.get(id) is not None:
			print(id,"Already Exists")
		else:
			name = input("Enter Name: ")
			add = input("Enter Address: ")
			data[id] = Person(name,add)
			print(id," Added")

	elif op == 2:
		for i in data:
			print("ID: ",i)
			data[i].display()
	
	elif op ==3 :
		id = int(input("Enter Id: "))
		if data.get(id) is not None:
			data.pop(id)
			print(id,"Deleted")
		else:
			print(id," Doesn't Exist")
	elif op ==4:
		break
	else:
		print("I dont understand")

