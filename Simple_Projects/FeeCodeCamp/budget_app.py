class Budget:
	def __init__(self,category):
		self.category = category
		self.ledger = []

	def check_fund(self,amount):
		balance = 0
		for x in self.ledger:balance += x['amount']
		return True if amount < balance else False

	def deposit(self,amount,description = ''):
		self.ledger.append({'amount':amount,'description':description})

	def widthraw(self,amount,description = ''):
		if self.check_fund(amount):
			self.ledger.append({'amount':-amount,'description':description})
			print(True)
		else: print(False)

	def get_balance(self):
		balance = 0
		for x in self.ledger:balance += x['amount'] 
		return balance

	def transfer(self,amount,description1,description2):
		if self.check_fund(amount) != None:
			for x in self.ledger:
				if x['description'] == description1:
					if x['amount'] < 0:x['amount'] += amount
					else:x['amount'] -= amount
				elif x['description'] == description2:
					if x['amount'] < 0:x['amount'] -= amount
					else:x['amount'] += amount
			print(True)
		else: print(False)

	def display(self):
		print(self.category.center(30,'*'))
		for x in self.ledger:
			print(str(x['description']).ljust(15,' '),str('{:.2f}'.format(x['amount'])).rjust(14,' '))
		print(f'Total: {self.get_balance()}')

if __name__ == '__main__':
	food = Budget('Food')
	food.deposit(1000,'Initial Fund')
	food.widthraw(100,'Groceries')
	food.widthraw(200,'Food Deliver')
	food.transfer(12,'Food Deliver','Groceries')
	food.display()