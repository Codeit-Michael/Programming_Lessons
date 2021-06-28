def arithmetic_arranger(*args):
	line1 = ''
	line2 = ''
	line3 = ''
	line4 = ''

	for x in args:
		num1,opt,num2 = x.split(' ')
		dict = {'+':int(num1) + int(num2),'-':int(num1) - int(num2),'*':int(num1) * int(num2),'/':int(num1) / int(num2)}
		line1 += f"{num1}".rjust(8,' ')
		line2 += f"{opt.ljust(3,(' '))}{num2}".rjust(8,' ')
		line3 += '   '.ljust(8,'-')
		line4 += f"{dict[opt]}".rjust(8,' ')
	print(line1)
	print(line2)
	print(line3)
	print(line4)

arithmetic_arranger('1 + 2','3 - 4','4678 / 4','98 * 9')