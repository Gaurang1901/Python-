#wapp to read 1st three letter day and print it its weekday or weekend

day = input("Enter day: ")

match day:
	case "mon"|"tue"|"wed"|"thu"|"fri":	print("Its Weekday")
	case "sat"|"sun":					print("Its Weekend")
	
	case _:	print("Invalid")