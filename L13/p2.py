#wapp to insert emp record

from sqlite3 import *
con  = None
try:
	con = connect("kit.db")
	cursor = con.cursor()
	sql = "select * from emp"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("id = ",d[0],"name = ",d[1])
except Exception as e:
	con.rollback()
	print("issue ",e)
finally:
	if con is not None:
		con.close()