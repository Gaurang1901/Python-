#wapp to find the sum of first "n" +ve no
n=int(input("Enter +ve no: "))
if n>=0:
	fact=1
	for i in range(1,n+1):
		fact*=i
	print("factorial of",n,"=",fact)
else:
	print("Invalid")
