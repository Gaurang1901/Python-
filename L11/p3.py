import os
filename = input("Enter Filename: ")
if os.path.exists(filename):
	try:
		with open(filename,"a") as f:
			data = input("Enter data: ")
			f.write(data+"\n")
	except Exception as e:
		print("issue ",e)
else:
	print(filename,"does not exist")


	