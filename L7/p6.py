#wapp to read set of names frm user for bday prty

names=set()

while True:
	op=int(input("1Add\n2:Remove\n3:View\n4:Exit\n: "))
	if op == 1:
		n=input("Enter Names: ")
		n=n.lower()
		r1=len(names)
		names.add(n)
		r2=len(names)
		if r2>r1:
			print("Added")
		else:
			print("Already Present")
	elif op ==2:
		n=input("Enter names for removal: ")
		n=n.lower()
		if n in names:
			names.discard(n)
			print(n,"Removed")
		else:
			print("Not Found")
	elif op==3:
		print(names)
	elif op==4:
		break
	else:
		print("Not allowed")

		
