#wapp to square root of number

print("Good Evening")
try:
	n1 = float(input("Enter 1st integer: "))
	res = n1 **0.5
	print("square root : ",res)
except ValueError:
	print("enter numbers")
except TypeError:
	print("enter +ve numbers")
print("Byee")