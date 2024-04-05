def ac(r):
	pi=22/7
	area=pi*r**2
	cir=2*pi*r
	print("Area=",round(area,2))
	print("Circumference=",round(cir,2))


r=float(input("Enter radius: "))
if r>0.0:
	ac(r)
else:
	print("invalid")