#Linear search

""" If we want the exact value instead of index; """
"""
def linear(li,target):
	for x in li:
		if x == target:
			return x
	return None
"""

""" Our objective is to return index position of the target 
if present, else returns none """

def linear(li,target):
	targeter = f'{target} is found at index {li.index(target)}'

	for x in range(0, len(li)):
		if li[x] == target:
			return targeter
	return None


if __name__ == '__main__':
	list1 = [1,2,3,4,5]
	name1 = ['fr','ty','uh','po','mo','do','ro']

	print(list1)
	result = linear(list1, 3)
	print(result)

	print(linear(name1, 'ty'))
