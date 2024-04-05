#wapp to divide two integers

print("Good Evening")
try:
	n1 = int(input("Enter 1st integer: "))
	n2 = int(input("Enter 2nd integer: "))
	res = n1 / n2
except ValueError:
	print("Pls enter integers")
except ZeroDivisionError:
	print("2nd integer shud not be 0")
else:
	print("res : ",res)
print("Byee")