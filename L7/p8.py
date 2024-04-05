#wapp to implement covid patients

cc = {}
while True:
	op = int(input("1:New\n2:View\n3:Update\n4:Remove\n5:Exit\n:"))
	
	if op == 1:
		s_nm=input("Enter Station Name: ")
		if cc.get(s_nm) is not None:
			print(s_nm,"already exist")
		else:
			count = int(input("enter count: "))
			cc[s_nm] = count
			print(s_nm,"Added")
	elif op == 2:
		print(cc)
	elif op ==3:
		s_nm=input("Enter Station Name: ")
		if cc.get(s_nm) is not None:
			count = int(input("enter count: "))
			cc[s_nm] = count
			print(s_nm,"Added")
		else:
			print("Not Found")
	elif op ==4:
		s_nm=input("Enter Station Name: ")
		if cc.get(s_nm) is not None:
			cc.pop(s_nm)
			print(s_nm,"removed")
		else:
			print("Not Found")
	elif op ==5:
		break
	else:
		print("sorry")