#wapp to read tuple of mrks frm user and print lowest nd highest mrks

mrks=()
res=input("do u want to enter some names y/n: ")
while res =="y":
	n=int(input("Enter mrks: "))
	mrks = mrks+(n,)
	res = input("do u want to enter some names y/n: ")

low=min(mrks)
high=max(mrks)
print("Low: ",low)
print("High: ",high)