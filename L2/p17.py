#wapp to check if given int is even or odd
#even == no%2 == 0
#2,4,6,8,10,....
#1,3,5,7,9,...
no=int(input("Enter a no: "))

match no%2:
	case 0: print("Even")
	case _: print("Odd")