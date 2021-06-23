class wage:
	def __init__(self,salary):
		self.salary = salary

	# getter decorator
	@property
	def cur_salary(self):
		return self.salary

	# setter decorator
	@cur_salary.setter
	def new_salary(self,wage):
		self.salary = wage

	# deleter decorator
	@cur_salary.deleter
	def zero_salary(self):
		del self.salary

d1 = wage(1000)
print(d1.cur_salary)
d1.new_salary = 2000
print(d1.salary)
