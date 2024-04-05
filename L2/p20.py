#wapp to check if given yr is leap or not

year=int(input("Enter year: "))

match year%4:
	case 0: print("Given year is leap year")
	case 1: print("Given year is not a leap year")
	case 2: print("Given year is not a leap year")
	case 3: print("Given year is not a leap year")