#wapp to read set of email address from user

email = set()

res = input("Do u want to enter email: ")
while res == "y":
	e=input("Enter email address: ")
	r1=len(email)
	email.add(e)
	r2=len(email)
	if r2>r1:
		print("Added")
	else:
		print("already Presnt")
	res = input("Do u want to enter more: ")

print(email)
