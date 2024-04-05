def sortt(s1):
	d1=sorted(s1)
	ns="".join(d1)
	return ns

s1=input("Enter 1st string: ")
s2=input("Enter 2nd string: ")


if sortt(s1) == sortt(s2):
	print("anagram")
else:
	print("Not a anagram")