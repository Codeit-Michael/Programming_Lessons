"""Sellection Sort- selects the smallest element, switch it
to the left most element, repeat doing it untill fully sorted

-considers the left part the sorted and right was the unsorted
EX: unsorted list
[2,4,1]
-quoted number represents the target no.
[] [2,4,"1"]
-switch it to the left most then bound
[1] [4,2]
-repeat
[1] [4,"2"]
[1,2] [4]
[1,2] ["4"]
[1,2,4] []

Its time complexity in worst and ave. is o(sqr(n)) or O(n*n)
-because it has 2 loops which is both linear
"""

def selSort(list):
	bit = []
	for x in range (0, len(list)):
		move = minimumIndex(list)
		bit.append(list.pop(move))
		print('%1s %-1s' % (bit,move))
	print(bit)
	return

def minimumIndex(list):
	minIndex = 0
	for x in range(1, len(list)):
		if list[x] < list[minIndex]:
			minIndex = x
	return minIndex


if __name__ == '__main__':
	mylist = [24,35,12,32,1,2,67,4]
	selSort(mylist)