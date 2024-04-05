#wamdp to track friends attending bday prty

names=[]
while True:
	op =int(input("1: Add\n2: Remove \n3: View \n4: Exit\n"))
	if op == 1:
		n=input("Enter name to be added: ")
		names.append(n)
		print("Added")
	elif op ==2:
		n=input("Enter name to be removed: ")
		if n in names:
			names.remove(n)
			print("Removed")
	elif op ==3:
		for i in names:
			print(i)
	elif op ==4:
		break
	else:
		print("sorry I dont understand ")