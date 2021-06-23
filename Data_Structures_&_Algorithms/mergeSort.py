def mergeSort(list):
	if len(list) <= 1:
		return list
	mid = len(list)//2
	left = mergeSort(list[:mid])
	right = mergeSort(list[mid:])
	print('%15s %1s %-15s' % (left, mid, right))
	sorted = []
	leftInd = 0
	rightInd = 0
	while leftInd < len(left) and rightInd < len(right):
		if left[leftInd] < right[rightInd]:
			sorted.append(left[leftInd])
			leftInd += 1
#			print('%15s %1s %-15s' % (left, mid, right))
		else:
			sorted.append(right[rightInd])
			rightInd += 1
#			print('%15s %1s %-15s' % (left, mid, right))
	sorted += left[leftInd:]
	sorted += right[rightInd:]
	return sorted

if __name__ == '__main__':
	mylist = [3,4,2,1,5,6,9,8,0]
	print(mergeSort(mylist))
