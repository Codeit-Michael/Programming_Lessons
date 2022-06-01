"""Test 1: Give a number and it will print all the numbers fro zero to the number given"""

from collections import deque
#You can use deque or list

def fLoop():
	num = int(input('enter number: '))
	li = deque([])
	for x in range(0,num+1):
		#appendleft if deque, insert if list
		li.appendleft(x)
	for items in li:print(items)
fLoop()

print('')

def wLoop():
	num = int(input('eneter number: '))
	rng = 0
	li = []
	while rng != num+1:
		li.insert(0, rng)
		rng += 1
	print(li)
	return
wLoop()
