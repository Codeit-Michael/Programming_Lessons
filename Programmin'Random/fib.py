def fib(rng,num):
	nums = num
	lastnum = 0
	for x in range(rng):
		nums += lastnum
		lastnum = nums
	return nums

print(fib(3,1))
