#wapp to read tuple of no frm user and print print tuple in desc order

data=()
res = input("Do u want to enter more y/n: ")
while res =="y":
	d = float(input("Enter number: "))
	data = data+(d,)
	res = input("Do u want to enter more y/n: ")

d1= tuple(sorted(data,reverse = True))
print(data)
print(d1)