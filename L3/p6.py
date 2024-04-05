#wapp to find the factorial of given no
n=int(input("Enter +ve no: "))
if n>=0:
	i=1
	fact=1
	while i<=n:
		fact=fact*i
		i=i+1
		
	print("Factorial of",n," =",fact)
else:
	print("Invalid")
