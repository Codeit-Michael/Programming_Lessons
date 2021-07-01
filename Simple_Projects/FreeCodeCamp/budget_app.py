class Category:
	def __init__(self,category):
		self.category = category
		self.ledger = []

	def check_fund(self,amount):
		balance = 0
		for x in self.ledger:balance += x['amount']
		return True if amount < balance else False

	def deposit(self,amount,description = ''):
		self.ledger.append({'amount':amount,'description':description})

	def withdraw(self,amount,description = ''):
		if self.check_fund(amount):
			self.ledger.append({'amount':-amount,'description':description})
			return True
		else: return False

	def get_balance(self):
		balance = 0
		for x in self.ledger:balance += x['amount'] 
		return '{:.2f}'.format(balance)

	def transfer(self,amount,other):
		if self.check_fund(amount):
			self.withdraw(amount)
			other.deposit(amount)
			return True
		else: return False

	def __str__(self):
		print(self.category.center(30,'*'))
		for x in self.ledger:
			print(str(x['description']).ljust(15,' '),str('{:.2f}'.format(x['amount'])).rjust(14,' '))
		return f'Total: {self.get_balance()}'

	def __repr__(self):
		return __str__

def create_spend_chart(li):
	num1,num2,index = 0,0,1
	percents = [['100|',' 90|',' 80|',' 70|',' 60|',' 50|',' 40|',' 30|',' 20|',' 10|','  0|','    ']]
	below = [[]]
	l1 = 0
	l2 = 0
	for x in li:
		for y in x.ledger:
			if y['amount'] > 0:num1 += y['amount']
			else:num2 -= y['amount']
		percents.append([])
		rng = ((num2/num1)*100//10)
		print(rng)
		for z in range(int('{:.0f}'.format(10-rng))):percents[index].append(' ')
		for z in range(int('{:.0f}'.format(1+rng))):percents[index].append('o')
		percents[index].append('-')
		index += 1
		num1,num2 = 0,0

	index = 1
	for x in range(15):
		below[0].append('    ')

	for x in li:
		below.append([])
		for y in x.category:
			below[index].append(y)
		for z in range(20-len(x.category)):
			below[index].append(' ')
		index += 1

	for x in range(12):
		for y in percents:
			print(y[x],end = ' ')
		print()

	for x in range(15):
		for y in below:
			print(y[x],end = ' ')
		print()

if __name__ == '__main__':
	utilities = Category('Utilities')
	utilities.deposit(200,'Initial Fund')
	utilities.withdraw(100,'Electricity Fee')
	utilities.withdraw(9.99,'New sink')
	utilities.deposit(100,'Additional Fund')
	utilities.withdraw(45.50,'Plummer Fee')

	food = Category('Food')
	food.deposit(1000,'Initial Fund')
	food.withdraw(150,'Groceries')
	food.withdraw(200,'5* restaurant')
	food.withdraw(160,'Food Deliver')
	food.transfer(20.50,utilities)
	food.withdraw(150,'Groceries')
	food.withdraw(150,'Food Deliver')
	food.withdraw(200,'Foods for Party')

	auto = Category('Auto')
	auto.deposit(300,'Intial Fund')
	auto.withdraw(100,'Twin Trubo')
	auto.withdraw(80.50,'Bagong Mags')
	auto.withdraw(40.99,'HKS Intercooler')
	auto.withdraw(20.99,'Lether Seats')

	print(utilities)
	print(food)
	print(auto)

	create_spend_chart([food,utilities,auto])

for x in range(3):
	for y in range(10):
		print('x',end = '')
	print()