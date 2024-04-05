#wapp to read 3 nos and print max of 3

rating=int(input("Enter 1st no: "))
match rating:
	case 5: print("Superb")
	case 4: print("Superb")
	case 3: print("Good")
	case 2: print("Good")
	case 1: print("Poor")
	case _: print("Ivalid")