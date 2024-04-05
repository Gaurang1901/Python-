def mini(n1,n2):
	if n1<n2:
		return n1
	else:
		return n2

n1=int(input("Enter 1st no: "))
n2=int(input("Enter 2nd no: "))
res=mini(n1,n2)
print("Min: ",res)