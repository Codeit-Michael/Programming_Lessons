"""Quick sort- gets the pivot, send to the mid the less than
the pivot and to the right the greater than the pivot
-to see the running time of an algo just: time python3 'filename.py' """

#mylist = [2,4,1,4,3,7,6,5,47,8,0,9]

mylist = [24,35,12,32,1,2,67,4]

name1 = ['fr','ty','uh','po','mo','do','ro']

def quickSort(list):
	if len(list) <= 1:
		return list

	leftValue = []
	rightValue = []
	pivot = list[0]

	for x in list[1:]:
		if x <= pivot:
			leftValue.append(x)
		else:
			rightValue.append(x)

	print('%15s %1s %-15s' % (leftValue, pivot, rightValue))
	return quickSort(leftValue) + [pivot] + quickSort(rightValue)

if __name__ == '__main__':
	print(quickSort(mylist))
	nameSort = quickSort(name1)
	print(nameSort)
