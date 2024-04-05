#wapp to add two integers
# Procedure Oriented Programming 

def add(n1,n2):
	res=n1+n2
	return res

n1=int(input("Enter 1st intger: "))
n2=int(input("Enter 2nd integer: "))
res=add(n1,n2)
print("result= ",res)