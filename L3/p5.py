#wapp to find the sum of first "n" +ve no
n=int(input("Enter +ve no: "))
if n>0:
	i,sum=1,0
	while i<=n:
		sum+=i
		i+=1
		
	print("Sum=",sum)
else:
	print("Invalid")
