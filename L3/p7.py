#wapp to find the factorial of given no
n=int(input("Enter +ve no: "))
if n>=0:
	fact,i=1,1
	
	while i<=n:
		fact*=i
		i+=1
		
	print("Factorial of",n," =",fact)
else:
	print("Invalid")
