def compute(n1,n2,n3):
	sum=n1+n2+n3
	avg=sum/3
	return sum,avg

n1=float(input("Enter 1st intger: "))
n2=float(input("Enter 2nd integer: "))
n3=float(input("Enter 3rd integer: "))
sum,avg=compute(n1,n2,n3)
print("Sum=",round(sum,2))
print("Avg=",round(avg,2))


