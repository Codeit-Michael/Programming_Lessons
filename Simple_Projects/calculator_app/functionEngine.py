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
	solution = {'+' : float(num1) + float(num2),
	'-' : float(num1) - float(num2),
	'*' : float(num1) * float(num2),
	'/' : float(num1) / float(num2)}
	return solution[opt]

if __name__ == '__main__':
	print(calc('5','-','2'))

