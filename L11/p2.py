import os
filename = input("Enter Filename: ")
if os.path.exists(filename):
	os.remove(filename)	
	print(filename," removed")
else:
	print(filename," does not exists")

	