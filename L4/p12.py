#wapp to read a string and check if its palindrome

s1=input("Enter String: ")
r1=s1[::-1]

if s1==r1:
	print("Yes")
else:
	print("No")