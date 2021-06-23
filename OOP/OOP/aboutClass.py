
"""
Classes Logic: think like classes has its own environment. Every object that
was created inside of it was all belongs to it even you might not seen they are
saved in a particular container but it still inside of the class and you can
access or modify them using object functions just make sure you put the self
parameter inside their conditions because it is the middle man between the objects
and the functions.
-The init() function was used to add objects inside the class. It automatically
run once the class was called.
-to avoid error without an empty cleass, just pass
Delete object priorities
-del p1.age
Delete Object
-del p1
"""
class Person:
	# values passed in parameters was converted into class objects
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Object methods (modifying objects through function)
	def myfunc(self):
		print(f'Hello my name is {self.name}, age is {self.age}')
#set it up like this
p1 = Person("Agg", 17)
#else
#p1.age = 17

print(p1.name,p1.age)
p1.myfunc()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#it will show all about the class
print(Person.__dict__)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

"""
def x(nums):
	for x in nums:
		print(x*2)
e = [1,2,3,4]
x(e)
