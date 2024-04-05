#wapp to track food order

diary=[]

res=input("wud u like to order something: y/n")
while res == "y":
	nm=input("Enter food name: ")
	diary.append(nm)
	res=input("ud u like to order more y/n")

print("food ordered: ",diary)
