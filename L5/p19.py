#wapp to read marks of students and find the min and max mrks

mrks=[]

res=input("do u want to enter marks: y/n: ")

while res =="y":
	m=int(input("enter mrks: "))
	mrks.append(m)
	res=input("do u want to enter more: ")

maxi=max(mrks)
mini=min(mrks)

print("maximum: ",maxi)
print("minimum: ",mini)