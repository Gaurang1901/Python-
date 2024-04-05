#wapp to read age nd wt of usr and check if usr can donate blood
#and min 25 and wt min 60

age=int(input("Enter Age: "))
wt=float(input("Enter Weight: "))

if age>=25 and wt>=60.0:
	print("Person can donate blood")
else:
	print("Person cannot donate blood")