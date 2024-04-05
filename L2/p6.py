#wapp to read amt in dollars and convert rs

dollars = float(input("Enter amt in dollars: "))

if dollars>0.0:
	rs=dollars*82
	print("\u20B9",round(rs,2),sep="")   #\u for unicode sep seprater
else:
	print("Invalid Amount")