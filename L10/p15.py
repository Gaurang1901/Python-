class Student:
	def __init__(self,rno,name,mrks):
		self.rno = rno
		self.name = name
		self.mrks = mrks
	def show(self):
		print("\nRoll  No: ",self.rno)
		print("Name: ",self.name)
		print("Marks : ",self.mrks)

try:
	r = int(input("Enter No: "))
	if r<0:
		raise Exception("Rno shold be +ve")
	n = input("Enter Name: ")
	if not n.isalpha():
		raise Exception("Name shold contain only alphabates")
	m = int(input("Enter Marks: "))
	if m<0 and m>100:
		raise Exception("Marks shold be +ve")	
	s = Student(r,n,m)
	s.show()
except ValueError:
	print("integers only")
except Exception as e:
	print(e)