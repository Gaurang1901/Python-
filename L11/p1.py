import os
filename = input("Enter Filename: ")
if os.path.exists(filename):
	print(filename," already exists")
else:
	try:
		with open(filename,"w") as f:
			print(filename," created")
	except Exception as e:
		print("issue ",e)

	