#wapp to creat a new file

import os
filename = input("Enter Filename: ")
if os.path.exists(filename):
	print(filename,"already exists")
else:
	f = None
	try:
		f = open(filename,"a")
		print("filename","created")
	except Exception as e:
		print("Issue",e)
	finally:
		if f is not None:
			f.close()