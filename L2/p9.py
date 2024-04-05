#wapp to read marks between 0 to 100 nd print grade
#m >80 =a,m>60=b,m>40=c else d

m=float(input("Enter Marks: "))

if m<0 or m>100:
	print("Invalid marks")
elif m>80:
	print("Grade A")
elif m>60:
	print("Grade B")
elif m>40:
	print("Grade c")
else:
	print("Grade D")