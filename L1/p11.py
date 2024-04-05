#wapp to read two no and print min of two no

n1=float(input("Enter 1st no: "))
n2=float(input("Enter 2nd no: "))
if n1>n2:
	print("Min value is n2: ",round(n2,2))
else:
	print("Min value is n1: ",round(n1,2))

print("Min = ",min(n1,n2))