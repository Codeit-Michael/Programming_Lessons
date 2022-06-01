from sys import argv


def divisible_by(x: int) -> list:
	return [i for i in range(1, x+1) if x % i == 0]

ry = [480,840,460,860]

for x in ry:
	print(divisible_by(x))

r = 32+24

print(1,r%2,r%4,r%8)
print(2,r%3,r%6,r%9)
print(3,r%5,r%6,r%7)
print(4,r%2,r%3,r%5)
