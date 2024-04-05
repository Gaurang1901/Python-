#wamdp to timplement Queue

queue=[]
while True:
	op =int(input("1: push\n2: pop \n3: View \n4: Exit\n"))
	if op == 1:
		n=input("Enter Element: ")
		queue.append(n)
		print("Added")
	elif op ==2:
		if len(queue)==0:
			print("Doesn't Exist")
		else:
			n1=queue.pop(0)
			print("Poped Element:",n1)
	elif op ==3:
			print(queue)
	elif op ==4:
		break
	else:
		print("sorry I dont understand ")