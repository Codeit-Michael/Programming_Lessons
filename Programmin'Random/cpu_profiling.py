import timeit
import cProfile
import random

def sort_expensive():
	the_list = random.sample(range(1_000_000), 1_000)
	the_list.sort()

def sort_cheap():
	the_list = random.sample(range(1_000), 10)
	the_list.sort()

if __name__ == "__main__":
	sort_expensive()
	for i in range(1000):
		sort_cheap()
	# tmt = timeit.timeit(stmt="sort_expensive()",globals=globals(),number=1)
	# tnt = timeit.timeit(stmt="sort_cheap()",globals=globals(),number=1000)
	# print(tmt)
	# print(tnt)


