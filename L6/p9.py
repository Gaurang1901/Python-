#wapp to read list of mrks and print lowest nd highest mrks

mrks = []

res = input("do u want to enter mrks y/n : ")
while res == "y":
	m=int(input("Enter Mrks: "))
	mrks.append(m)
	res = input("do u want to enter more y/n: ")

sum = 0
avg = 0

#j=len(mrks)
#for i in range(0,j):
#	sum+=mrks[i]
#avg=sum/len(mrks)
#print("avg = ",round(avg,2))

for i in mrks:
	sum=sum+i
avg=sum/len(mrks)
print("avg = ",round(avg,2))