# iterative
def iterative_search(list,target):
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = (low+high)//2
		if list[mid] > target:
			high = mid - 1
		elif list[mid] < target:
			low = mid + 1
		elif list[mid] == target:
			return f'{target} found at index {list.index(target)}'
		else:
			return None

# recursive
def recursive_search(list, target):
	if len(list) == 0:
		return True
	mid = len(list)//2

	if list[mid] == target:
		return f'{target} found at index {list.index(target)}'
	elif target not in list:
		return None
	elif list[mid] > target:
			return recursive_search(list[:mid], target)
	else:
		return recursive_search(list[mid:], target)

if __name__ == '__main__':
	mylist = [1,2,3,4,5,6,7,8,9,10]
	print(iterative_search(mylist,6))
	print(recursive_search(mylist,2))