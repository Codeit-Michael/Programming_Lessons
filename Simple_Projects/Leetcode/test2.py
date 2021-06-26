"""reverse, add, then save as a list"""

def join_solution(list1,list2)
:	list1.reverse()
	list2.reverse()
	var1 = int(''.join([str(elem) for elem in list1]))
	var2 = int(''.join([str(elem) for elem in list2]))
	return var1 + var2


def map_solution(list1,list2):
	list1.reverse()
	list2.reverse()
	var1 = int(''.join(map(str, list1)))
	var2 = int(''.join(map(str, list2)))
	return var1 + var2

l1 = [1,2,3,4,5]
l2 = [4,5,6]

print(join_solution(l1,l2))

# whe're checking if the answer given is correct
print(54321 + 654)