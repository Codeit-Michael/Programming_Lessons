#regular method >> self parameter, @classmethod >> cls, @staticmethod >> None
class Person:
	emps = 0
	raiseNum = 1.04
	def __init__(self,name,last,wage):
		self.name = name
		self.last = last
		self.wage = wage
		Person.emps += 1

	#use when we are working with the class variable, cls instead of self
	@classmethod
	def raiseSetter(cls, data):
		cls.raiseNum = data

	#class method constructor example: splits a str every '-'
	@classmethod
	def splitter(cls,strs):
		first,last,wage = strs.split('-')
		return cls(first,last,wage)


	#independent(doesn't need a starting parameter like self/cls bc it works on its own)
	#can access with/without object; print(Person(isWorkday(4)))
	@staticmethod
	def isWorkday(day):
		if day < 5:
			return True
		return False

e1 = Person('Agg','Maranan',16)
e2 = Person('Ag','Maranann',18)
ee = 'dr-dre-70'
ei = Person.splitter(ee)
#print(ei.name)


print(Person.raiseNum)
#now we set the raiseNum val to 1.05
Person.raiseSetter(1.05+4)
print(Person.raiseNum)

er = Person.isWorkday(3)
print(er)
