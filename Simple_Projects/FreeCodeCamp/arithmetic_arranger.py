def arithmetic_arranger(*args):

	new1 = []
	inds = 0
	for x in args:
		num1,opt,num2 = x.split(' ')
		dict = {'+':int(num1) + int(num2),'-':int(num1) - int(num2),'*':int(num1) * int(num2),'/':int(num1) / int(num2)}
		new1.append([])
		new1[inds].append(f"{num1}".rjust(8,' '))
		new1[inds].append(f"{opt.ljust(3,(' '))}{num2}".rjust(8,' '))
		new1[inds].append('   '.ljust(8,'-'))
		new1[inds].append(f"{dict[opt]}".rjust(8,' '))
		inds += 1

	for x in range(4):
		for y in new1:
			print(y[x],end = '')
		print()

arithmetic_arranger('1 + 2','3 - 4','4678 / 4','98 * 9')
