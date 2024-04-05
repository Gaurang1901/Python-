#wapp to chant some mantra
#DRY => Do Repeat Yourself

def chant():
	print("Hare Krishna")
	print("Hare Rama")
	print("Hare Hare\n")

n=int(input("Enter +ve no: "))

if n > 0:
	for i in range(1,n+1):
		chant()
else:
	print("Invalid")