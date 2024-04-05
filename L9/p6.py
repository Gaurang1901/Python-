class Emp:
    def __init__(self,id,name,add,sal):
        self.id = id
        self.name = name
        self.add = add
        self.sal = sal
    def show(self):
        print("Id = ",self.id)
        print("Name= ",self.name)
        print("Address= ",self.add)
        print("Salary= ",self.sal)
    def bonus(self):
        amt = self.salary*0.10
        print("bonus amt = ",amt)

class JD(Emp):
	j = JD(10,"PK","dadar","100000")
	j.show()
	j.bonus()

class SD(Emp):
    def bonus(self):
        amt = self.sal*0.15
        print("bonus amt= ",amt)

s= SD(15,"GK","Virar",200000)
s.show()
s.bonus()

class Mgr(Emp):
    def bonus(self):
        amt = self.sal*0.20
        print("bonus amt= ",amt)

s= SD(15,"VGK","Virar",300000)
s.show()
s.bonus()