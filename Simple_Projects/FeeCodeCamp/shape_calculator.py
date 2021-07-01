class Rectangle:
	def __init__(self,width = None,height = None):
		self._width = width
		self._height = height

	def __str__(self):
		return f'Rectangle(width={self._width},height={self._height})'

	def __repr__(self):
		return __str__

	def set_width(self,width):
		self._width = width

	def set_height(self,height):
		self._height = height

	def get_area(self):
		return self._width * self._height

	def get_perimeter(self):
		return (2*self._width) + (2*self._height)

	def get_diagonal(self):
		return (self._width**2 + self._height**2)**0.5

	def get_picture(self):
		if self._width > 50 or self._height > 50:
			return 'Too big for picture'
		for x in range(self._height):
			for y in range(self._width):
				print('*',end = '')
			print()
		return ('')

	def get_amount_inside(self,other):
		height,width = 0,0
		my_width,my_height = self._width,self._height
		your_width,your_height = other._width,other._height

		while my_height != your_height or my_width != your_width:
			if my_height > your_height:
				your_height += other._height
				height += 1

			elif your_height > my_height:
				my_height += self._height
				height += 1

			elif my_width > your_width:
				your_width += other._width
				width += 1
			else:
				my_width += self._width
				width += 1
		total = (height+width)*2
		return total

class Square(Rectangle):
	def __init__(self,side):
		self._width = side
		self._height = side

	def set_side(self,side):
		self._width = side
		self._height = side

if __name__ == '__main__':
	rect = Rectangle(10, 5)
	print(rect.get_area())
	rect.set_height(3)
	print(rect.get_perimeter())
	print(rect)
	print(rect.get_picture())
	 
	sq = Square(9)
	print(sq.get_area())
	sq.set_side(4)
	print(sq.get_diagonal())
	print(sq)
	print(sq.get_picture())

	rect.set_height(8)
	rect.set_width(16)
	print(sq.get_amount_inside(rect))
