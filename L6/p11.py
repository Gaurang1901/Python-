#wamdp to timplement stack

stack=[]
while True:
	op =int(input("1: push\n2: pop \n3: View \n4: Exit\n"))
	if op == 1:
		n=input("Enter Element: ")
		stack.append(n)
		print("Added")
	elif op ==2:
		n=input("Enter element to be poped: ")
		if len(stack)==0:
			print("Doesn't Exist")
		else:
			stack.pop()
			print("Poped Element:",n)
	elif op ==3:
			print(stack)
	elif op ==4:
		break
	else:
		print("sorry I dont understand ")