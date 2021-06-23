# Encapsulation example
class developer:
	def __init__(self,name,age):
		self.name,self.age = name,age
		self._salary = None # (protected atts-can access in & outside the class but hidden)
		self.__bounty = 0 # (private atts-only methods can access)

	def bounty(self):
		self.__bounty += 1

	# accessing protected inside
	#you can access it outside by: print(p1._salary)
	def salaries(self): # getter
		return self._salary

	#setting protected inside
	#setting outside: p1._salary = wage
	def change_salary(self,wage): # setter
		self._salary = self.total(wage)

	# this is the private method here. There's no way to access this outside
	# you can done this method in self._1underscore/self.__2underscore
	def total(self,wage):
		if self.__bounty >= 1:
			return wage * 2
		return wage

p1 = developer('Ernest',17)
p1.change_salary(100)
print(p1.salaries())
p1.bounty()
p1.change_salary(100)
print(p1.salaries())

