#wapp to square root of number

print("Good Evening")
try:
	n1 = float(input("Enter 1st integer: "))
	res = n1 **0.5
	print("square root : ",round(res,2))
except (ValueError,TypeError):	
	print("enter +ve numbers")
print("Byee")