#wapp to read set of email address from user

email = set()

res = input("Do u want to enter email: ")
while res == "y":
	e=input("Enter email address: ")
	email.add(e)
	res = input("Do u want to enter more: ")

print(email)
