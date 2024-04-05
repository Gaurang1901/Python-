class book:
	def __init__(self,id,title,author,price):
		self.id = id
		self.title = title
		self.author = author
		self.price = price
	
	def show(self):
		print("Id : ",self.id)
		print("Title : ",self.title)
		print("Author : ",self.author)
		print("price : ",self.prince)
	def __add__(self,other):
		res = self.price+other.price
		return res

	def __sub__(self,other):
		res = self.price-other.price
		return res

	def __mul__(self,other):
		res = self.price*other.price
		return res

b1 = book(10,"ML","KS",500)
b2 = book(20,"DJ","KS",800)

r1 = b1+b2
print(r1)

r2 = b1-b2
print(r2)

r3 = b1*b2
print(r3)

