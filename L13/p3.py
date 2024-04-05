#wapp to insert emp record

from sqlite3 import *
con  = None
try:
	con = connect("kp.db")
	cursor = con.cursor()
	sql = "insert into book values('%d','%s','%s','%f')"
	bid = int(input("enter Emp Id: "))
	title = input("enter title:  ")
	author = input("enter Author:  ")
	price = float(input("Enter price: "))
	cursor.execute(sql %(bid,title,author,price))
	con.commit()
	print("Record Created")
except Exception as e:
	con.rollback()
	print("issue ",e)
finally:
	if con is not None:
		con.close()