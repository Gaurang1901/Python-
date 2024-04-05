#wapp to implement chatbot

conv = {
	"hello":"hii",
	"hii":"hellooo",
	"how r u":"fine",
	"thank u":"welcm",
	"bye":"Byee Have a great day",
	}
	
while True:
	op = input("enter ur question and press q to quit: ")
	if op =="q":
		break
	elif conv.get(op) is not None:
		ans=conv.get(op)
		print(ans)
	else:
		print("Sorry I dont Understand")