#wapp to read len and breadth and print area and perimeter of rect


len=float(input("Enter Length: "))
bre=float(input("Enter breadth: "))

area =len*bre
perimeter=2*(len+bre)
print("Area = ",round(area,2))
print("perimeter = ",round(perimeter,2))