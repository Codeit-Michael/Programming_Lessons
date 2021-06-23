# Property Decorators (Getter, Setter, Deleter)

class Person:
	def __init__(self,name,last):
		self.name = name
		self.last = last

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	"""it allows us to call a class function like an object like how we call
	the name object; print(p1.name)"""

	@property	# property decorator
	def email(self):
		return f'{self.name}{self.last}@gmail.com'

	@property	# property decorator
	def fullNm(self):
		return f'{self.name} {self.last}'


	# setter -to modify a function without errors;and accomplish the job
	# like how to set an object: p1.name = 'Kel'
	# this one modifies your full name function
	@fullNm.setter
	def fullNm(self,nm):
		name,last = nm.split(' ')
		self.name = name
		self.last = last


	# deleter
	@fullNm.deleter
	def fullNm(self):
		print('Names deleted')
		self.name = None
		self.last = None
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	def __repr__(self):
		return f'{self.fullNm'

p1 = Person('Agg','Maranan')


p1.fullNm = 'Kell Maranan'
print(p1)
#p1.name = 'Ikel'

