#wapp to add two add two integers

print("Good Evening")
try:
	n1 = int(input("Enter 1st integer: "))
	n2 = int(input("Enter 2nd integer: "))
	res = n1 + n2
except ValueError:
	print("Pls Enter Integer")
else:
	print("res : ",res)
print("Byee")