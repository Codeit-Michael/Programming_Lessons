class library_operations:
	def __init__(self):
		self.books = []

	def put_books(self,book):
		self.books.append(book)

	def borrow_book(self,book):
		if len(self.books) != 0:
			if book in self.books:
				return book
			else:
				None
		else:
			None

	def remove_book(self,book):		
		if len(self.books) != 0:
			if book in self.books:
				self.books.remove(book)
			else:
				None
		else:
			None

if __name__ == '__main__':
	agg = library_operations()
	agg.put_books('NARASHIMA- Practices of the python pro')
	print(agg.borrow_book('NARASHIMA- Practices of the python pro'))
	agg.remove_book('NARASHIMA- Practices of the python pro')