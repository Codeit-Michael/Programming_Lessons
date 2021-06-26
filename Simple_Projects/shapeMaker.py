# Makes a diamond shape from '*'
# its size is based the given number

def shape_maker(num):
	spc = ' '
	char = '*'
	real_num_val = num
	char_multiplier = 1

	for x in range(num):
		print(spc * num, char * char_multiplier)
		num -= 1
		char_multiplier += 2

	for x in range(real_num_val+1):
		print(spc * num, char * char_multiplier)
		num += 1 
		char_multiplier -= 2

shape_maker(4)