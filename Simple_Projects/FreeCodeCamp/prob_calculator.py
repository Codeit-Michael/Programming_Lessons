import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self,**kwargs):
		self.contents = []
		for x in kwargs:
			for y in range(kwargs[x]):
				self.contents.append(x)

	def draw(self,rng):
		return random.sample(self.contents,k=rng)

def experiment(hat,expected_balls=None,num_balls_drawn=None,num_experiments=None):
	copy.copy(hat)
	set_expected = []
	probability = 0
	for x in expected_balls:
		for y in range(expected_balls[x]):
			set_expected.append(x)

	for tries in range(num_experiments):
		for x in set_expected:
			if x in hat.draw(num_balls_drawn):
				probability += 1
	return probability

if __name__ == '__main__':
	hat = Hat(blue=4, red=2, green=6)
	probability = experiment(hat=hat,expected_balls={"blue": 2,"red":1},num_balls_drawn=4,num_experiments=3000)
	print("Probability:", probability)
