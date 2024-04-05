#wapp to read list of mrks and print lowest nd highest mrks

mrks = []

res = input("do u want to enter mrks y/n : ")
while res == "y":
	m=int(input("Enter Mrks: "))
	mrks.append(m)
	res = input("do u want to enter more y/n: ")

#print("Minimum mrks: ",min(mrks))
#print("Maximum mrks: ",max(mrks))
mrks.sort()
print("Minimum mrks: ",mrks[0])
print("Maximum mrks: ",mrks[-1])
