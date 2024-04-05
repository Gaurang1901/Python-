#wapp to read a string and count the no of letters and digits

data = input("Enter a String: ")

c1,c2=0,0

for i in data:
	if i.isalpha():
		c1+=1
	elif i.isdigit():
		c2+=1

print("C1= ",c1)
print("C2= ",c2)