#wapp to find the sum of first "n" +ve no
n=int(input("Enter +ve no: "))
if n>0:
	i=1
	sum=0
	while i<=n:
		sum=sum+i
		i=i+1
		
	print("Sum=",sum)
else:
	print("Invalid")
