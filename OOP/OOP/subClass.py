"""inheritance- creating subclasses
-inheriting methods and attributes from the parent classes
"""
#lets say we're making a programmer and manager class
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


#instead of copying the whole code, we must do a subclass
class developer(Person):
	#anything you modify from class vars inside the inherit class stays inside the inherit class only like:
	raiseNum = 3
	#adding more objects
	def __init__(self,name,last,salary,lang):
		#to keep the remaining data
		super().__init__(name,last,salary)
		self.lang = lang
		#now lets add progamming language to the objects

e1 = developer('Agg','Maranan',1000,'python')
e2 = developer('Ag','Maranann',2000,'ruby')
print(e1.fullNm(),e1.lang)
print(e2.fullNm(),e2.lang)
#print(help(developer)) for more infos
print('\n')

class manager(Person):
	def __init__(self,name,last,salary,employees=None):
		super().__init__(name,last,salary)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees

	def addEmp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def rmEmp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def empList(self):
		for emps in self.employees:
			print('>>',emps.fullNm())

mg1 = manager('Pu','La',8000,[e1])
mg1.empList()
print('')
mg1.addEmp(e2)
mg1.empList()

#tells us if it is an instance of the said class
#it is instance of Person and manager but not in developer
print(isinstance(mg1,developer))

#tells us if it is a subclass of the said class
print(issubclass(developer, Person))

print('')
"""
if we want to make a subclass that takes object attributes and
some of it was already exist on the super class; instead of doing
self. to them individually, you can use super().__init__(attributes)
EX:"""
class postman(Person):
	def __init__(self,name,last,salary,post_office):
		super().__init__(name,last,salary)
		self.post_office = post_office

	def __str__(self):
		return f'{self.name} {self.last}, {self.salary}, {self.post_office}'
pm1 = postman('agg','nanaram',7000,'amadeo branch')

print(pm1)

print('')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""Polymorphism example"""
class fruits:
	taste = 'sweet'
	pass


class orange(fruits):
	taste = 'sour'
	pass

print(fruits.taste)
print(orange.taste)
