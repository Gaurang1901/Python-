#wapp to create employee record
from pymongo import *
con  = None
try:
	con = MongoClient("localhost",27017)
	db=con["test1"]
	coll=db["employee"]

	i = int(input("Enter Emp ID:"))
	count = coll.count_documents({"_id":i})
	if count == 1:
		print(i," already exists")
	else:
		name = input("Enter name:	 ")
		salary = float(input("enter salary:"))
		info = {"_id":i,"name":name,"salary":salary}
		coll.insert_one(info)
		print(i," created")
except Exception as e:
	print("issue ",e)
finally:
	if con is not None:
		con.close()