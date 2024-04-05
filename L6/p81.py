marks = []
res = input("do u want to enter marks y/n ")
while res=="y":
	m = int(input("enter marks "))
	marks.append(m)
	res = input("do u want to enter more y/n ")
 
print(marks)