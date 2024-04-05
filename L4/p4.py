#wapp to read usrnme and pass
from getpass import *
un= input("Enter Username: ")
pas = getpass("Enter Password: ")

if un=="gaurang" and pas=="RedX":
	print("Success")
else:
	print("Failure")