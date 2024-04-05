data=input("enter a string: ")
data=data.lower()
d1=sorted(data)
print(d1)

ndata = "".join(d1)
print(ndata)

print("org=",data)
print("Sorted= ",ndata)