#wapp to creat a new file

import os
filename = input("Enter Filename: ")
if os.path.exists(filename):
	f = os.remove(filename)
	print(filename,"Deleted")
else:
	print(filename,"does not exist")