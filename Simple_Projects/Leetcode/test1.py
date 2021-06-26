""" Problem1 - add 2 numbers from the array that give you the answer
equivalent to target """

def find_solution(list,target):
	for i in range(list[-1]):
		vars = []
		ind = i+1
		if i + ind == target:
			vars.append(i)
			vars.append(i+1)
	return vars

l1 = [1,2,3]
print(find_solution(l1,5))
