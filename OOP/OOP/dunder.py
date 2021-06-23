#Magic methods/Double Underscore (Dunder)

class Person:
	emps = 0
	raiseNum = 1.04
	def __init__(self,name,last,salary):
		self.name = name
		self.last = last
		self.salary = salary
		Person.emps += 1

	def fullNm(self):
		return '%1s %-1s'%(self.name,self.last)

	def addBns(self):
		return int(self.salary*self.raiseNum)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	# useful for debugging something
	def __repr__(self):
		return f'People({self.name} ,{self.last} ,{self.salary})'

	# converts anything to a more understandable code output
	def __str__(self):
		return f'{self.fullNm()} - salary = {self.salary}'

	"""the repr maybe ignored if you had str but you can call them if you want to
	by print(repr/str(object name)) or print(p1.__repr__())"""

	# this kind of functions automatically run if use if you ad str or int
	# ex, it works like this: print(int.__add__(2,1))
	# we gonna use it to add their salaries
	def __add__(self, other):
		return self.salary + other.salary

	# compares objects, etc.
	# this example compares our 2 objects if they're the same
	# compares the objects 'last'
	def __eq__(self, other):
		return self.last == other.last

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
p1 = Person('Agg','Maranan',30000)
p2 = Person('Ikel','Maranan',50000)

#print(repr(p1))
print(p1)
#add dunder
print(p1+p2)
#eq dunder
print(p1 == p2)
