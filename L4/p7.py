#wapp to read a string and count the no of alpha and digit and other char

data = input("Enter a String: ")

c1,c2,c3=0,0,0

for i in data:
	if i.isalpha():
		c1+=1
	elif i.isdigit():
		c2+=1
	else:
		c3+=1

print("C1= ",c1)
print("C2= ",c2)
print("C3= ",c3)