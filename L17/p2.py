class Queue:
	def __init__(self):
		self.data = []

	def enq(self, ele):
		self.data.append(ele)
		print(ele, "is pushed on queue ")
	
	def deq(self):
		if len(self.data) == 0:
			print("queue is empty ")
		else:
			ele = self.data.pop(0)
			print("queue ele = ", ele)

	def show(self):
		print(self.data)

s = Queue()
while True:
	op = int(input("1:Enqueue\n2:Dequeue\n3:show\n4:exit "))
	if op == 1:
		ele = int(input("enter element "))
		s.enq(ele)
	elif op == 2:
		s.deq()
	elif op == 3:
		s.show()
	elif op == 4:
		break
	else:
		print("sorry i dont understand ")