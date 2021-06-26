def mergeSort_lists(list1,list2):
	list1.extend(list2)
	list1.sort()
	mid = len(list1) // 2
	left = list1[:mid]
	right = list1[mid:]
	if len(left) == len(right):
		return (left[-1] + right[0]) / 2
	else:
		return right[0] 

list1 = [0,1]
list2 = [3,4,2]
print(mergeSort_lists(list1,list2))