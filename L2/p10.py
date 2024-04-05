#wapp to read 3 nos and print max of 3

n1=float(input("Enter 1st no: "))
n2=float(input("Enter 2nd no: "))
n3=float(input("Enter 3rd no: "))

if n1>n2 and n1>n3:
	print("Max = ",n1)
elif n2>n1 and n2>n3:
	print("Max= ",n2)
else:
	print("Max= ",n3)