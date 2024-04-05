#wapf to welcome the user with some greet
#name & msg ==> formal par
#gaurang, gud morning == actual par

def greet(name,msg):
	res="Welcome "+name+" "+msg
	print(res)

#greet()
#greet("gaurang")

greet("gaurang","gud morning")
greet("gud morning","gaurang")

greet(name="gaurang",msg="gud morning")
greet(msg="gud morning",name="gaurang")