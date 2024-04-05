import math
r = float(input("Enter radius: "))
if r>0:
	area = math.pi*math.pow(r,2)
	circ = 2*math.pi*r
	print("Area : ",round(area,2))
	print("Circumference : ",round(circ,2))
else:
	print("Invalid radius")
