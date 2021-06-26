def calc(numset1,opt,numset2):
	# asks if operation is > 1, then it will throw an error
	if len(opt) > 1:
		return ('ERROR: more than one operations chosen')
	num1 = ''
	num2 = ''

	# converts 2 numbersets into 2 individual numbers
	# applicable wether numbersets are list/s or not
	for nums in numset1:
		num1 += nums
	for nums in numset2:
		num2 += nums

	# setting the numbersets and operations into problems
	add = float(num1) + float(num2)
	subtract = float(num1) - float(num2)
	multiply = float(num1) * float(num2)
	divide = float(num1) / float(num2)

	# asks about the operation choosed
	# depends here what willbe the answer
	if opt[0] == '+':
		return add
	elif opt[0] == '-':
		return subtract
	elif opt[0] == '*':
		return multiply
	elif opt[0] == '/':
		return divide
	else:
		return SyntaxError

if __name__ == '__main__':
	print(calc('5','-','2'))

