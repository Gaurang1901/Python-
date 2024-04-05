#wapp to read 1st three letter day and print it its weekday or weekend

day = input("Enter Day: ")

if day=="mon" or day=="tue" or day=="wed" or day=="thu" or day=="fri":
	print("Its a Weekday")
elif day=="sat" or day=="sun":
	print("Its a weekend")
else:
	print("Invalid")