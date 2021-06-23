"""Bogo Sort- picks randomly untill an array is sorted
Its time complexity is unknown because it can be solve in
any form of complexity"""

import random

mylist = [21,4,3,7,6,5,12,1]

def isSorted(list):
	for index in range(len(list)-1):
		if list[index] > list[index + 1]:
			return False
	return True

def bogo(list):
	attempts = 0
	while not isSorted(list):
		random.shuffle(list)
		attempts += 1
		print('%1s %-3s' % (attempts,list))
	print(list)
	print(f'sorting attempts: {attempts} times')
	return

if __name__ == '__main__':
	bogo(mylist)
