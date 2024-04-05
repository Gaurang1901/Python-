#wapf to find factorial of no

def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	print("Factorial = ",f)



n=int(input("Enter No:"))

if n>=0:
	f=fact(n)
else:
	print("Invalid")