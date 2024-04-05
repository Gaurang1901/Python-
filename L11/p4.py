import os
filename = input("Enter Filename: ")
if os.path.exists(filename):
	try:
		with open(filename,"r") as f:
			data = f.read()
			print(data)
	except Exception as e:
		print("issue ",e)
else:
	print(filename,"does not exist")


	