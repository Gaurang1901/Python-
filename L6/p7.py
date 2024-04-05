#wapp to read list of integers from the users dn print on the screen

data = []

res = input("do u want to enter integers y/n: ")

while res == "y":
	d = int(input("Enter Integers: "))
	data.append(d)
	res = input("do u want to enter more y/n: ")

print(data)

for d in data:
	print(d)