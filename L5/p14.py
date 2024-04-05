
def ap(l,b):
	
	area=l*b
	per=2*(l+b)
	print("Area=",round(area,2))
	print("Perimeter=",round(per,2))


l=float(input("Enter Length: "))
b=float(input("Enter Bredth: "))
if l>0.0 and b>0.0:
	ap(l,b)
else:
	print("invalid")