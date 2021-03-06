class calculator:
	# required inputs
	def __init__(self,num1=None,num2=None):
		self.num1 = num1
		self.num2 = num2

	# the main operation
	def compute(self,numset1,opt,numset2):
		# asks if operation is > 1, then it will throw an error
		if len(opt) > 1:
			return SyntaxError

		# if not it sets the required inputs into strings
		self.num1 = ''
		self.num2 = ''

		# converts 2 numbersets into 2 individual numbers
		# applicable wether numbersets are list/s or not
		for nums in numset1:
			self.num1 += nums
		for nums in numset2:
			self.num2 += nums

		# setting the numbersets and operations into problems
		solutions = {'+' : float(self.num1) + float(self.num2),
		'-' : float(self.num1) - float(self.num2),
		'*' : float(self.num1) * float(self.num2),
		'/' : float(self.num1) / float(self.num2)}
		return solutions[opt]

if __name__ == '__main__':
	new1 = calculator()
	print(new1.compute('1','+','3'))