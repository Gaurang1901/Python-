#wapp to read 1st three letter day and print it its weekday or weekend

day = input("Enter Day: ")

match day:
	case "mon":	print("Its Weekday")
	case "tue":	print("Its Weekday")
	case "wed":	print("Its Weekday")
	case "thu":	print("Its Weekday")
	case "fri":	print("Its Weekday")
	case "sat":	print("Its Weekend")
	case "sun":	print("Its Weekend")
	case _:	print("Invalid")