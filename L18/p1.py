class Graph:
	def __init__(self):
		self.info = {}

	def add(self,start,end):
		if start in self.info:
			self.info[start].append(end)
		else:
			self.info[start] = [end]
	def show(self):
		for i in self.info:
			print("NODE:",i)
			for j in self.info[i]:
				print(i,"-",j)

g= Graph()
while True:
	op = int(input("1:Add\n2:Show\n3:Exit\n:"))
	if op ==1:
		start = input("Enter start Node: ")		
		end = input("Enter End Node: ")
		g.add(start,end)
	elif op ==2:
		g.show()
	elif op==3:
		break
	else:
		print("Invalid")
	