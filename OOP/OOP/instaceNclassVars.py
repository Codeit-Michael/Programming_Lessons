class Person:
	emps = 0
	raiseNum = 1.04
	def __init__(self,name,last,age,salary):
		self.name = name
		self.last = last
		self.age = age
		self.salary = salary
		Person.emps += 1

	def fullNm(self):
		return '%1s %-1s'%(self.name,self.last)

	def addBns(self):
		return int(self.salary*self.raiseNum)

e1 = Person('Agg','Maranan',16,1000)
e2 = Person('Ag','Maranann',18,2000)

e1.raiseNum = 1.05
print(e1.__dict__)
print(e2.__dict__)

"""
-in this case the e1 has its own raiseNum val bc we set its raiseNum in 1.05
-we see in print(e1.__dict__)that e1 has own raiseNum unlike the e2
-our instance is everything about them and our class is the raiseNum because
-they had the same value for class variables instead we set one of them but it
is still class 
variable if we had other class objects without raiseNum
"""
print(e1.raiseNum)
print(e2.raiseNum)
print(Person.raiseNum)
print(Person.emps)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""instance variable(unique specs) and class variable(related specs)
example We had:
class cars:
	brand = 'Ferrari'
	def __init__(self, model):
		self.model = model
	def model(self):
		return self.model
c1 = cars(458)
c2 = cars(488)
print(c1.brand)
print(c1.model)
print(c2.brand)
print(c2.model)

in this case our class variable is Ferrari because they are both made by ferrari
"""

