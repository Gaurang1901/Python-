#wapp to find the sum of first "n" +ve no
n=int(input("Enter +ve no: "))
if n>0:
	sum=0
	for i in range(1,n+1):
		sum+=i
	print("Sum=",sum)
else:
	print("Invalid")
