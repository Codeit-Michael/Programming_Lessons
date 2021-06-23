"""A simple example of a working recursion"""
def add(numb):
	if numb >= 100:
		return numb
	else:
		numb += numb
		print(numb)
		add(numb)

add(34)

mylist = [1,2,3,4,5,6,7,8]

#function that adds every element in an array using loop, O(n)
def manualAdd(list):
	added = 0
	for x in list:
		added += x
	print(added)

#function same above but this use recursion
#it uses the base case to stop returning the command over n over
def recAdd(list):
	#means if not in list, then shut it down
	if not list:
		return 0
	print("calling sum(%s)" % list[1:])
	itemsLeft = recAdd(list[1:])
	print("call to sum(%s) returnin %d + %d" % (list,list[0], itemsLeft))
	return list[0] + itemsLeft

recAdd(mylist)
