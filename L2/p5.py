#wapp to read radius frm usr and print area and circumference of circle

radius=float(input("Enter Radius of circle: "))

if radius > 0.0:
	pi=22/7
	area= 3.14*radius*radius
	cir= 2*3.14*radius
	print("Area of circle = ",round(area,2))
	print("Circumference of circle = ",round(cir,2))
else:
	print("Invalid Radius")