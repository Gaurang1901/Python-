
rating=int(input("Enter rating: "))
if rating<0 or rating>5:
	print("Invalid")
elif rating == 5 or rating == 4:
	print("Superb")
elif rating == 3 or rating == 2:
	print("Good")
else:
	print("Poor")