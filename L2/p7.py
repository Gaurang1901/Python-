#wapp to read length and breadth frm usr & print area dn perimeter of rectangle

len=float(input("Enter length: "))
bre=float(input("Enter Breadth: "))

if len>0.0 and bre>0.0:
	area=len*bre
	peri=2*(len*bre)
	print("Area of Rectangle: ",round(area,2))
	print("Perimeter of Rectangle: ",round(peri,2))
else:
	print("Invalid Values")