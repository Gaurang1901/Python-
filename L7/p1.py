#wapp to read tuple of names from user and print on the screen

names=()
res=input("do u want to enter some names y/n: ")
while res =="y":
	n=input("Enter name: ")
	names = names+(n,)
	res = input("do u want to enter some names y/n: ")

print(names)
for n in names:
	print(n)