# Simple computerized movie renting transaction
# Expect the movie is the time self.moive_durationn 

import time


class movie_world:
	def __init__(self):
		self.movie_amount = 100
		self.movie_duration = 3
		self.paid = False

	def play_movie(self):
		print('Payment first before accessing the movie...')
		while self.paid != True:
			self._payment_transaction()

		t = self.movie_duration
		while t:
			mins, secs = divmod(t, 60)
			timer = '{:02d}:{:02d}'.format(mins, secs)
			print(timer, end="\r")
			time.sleep(1)
			t -= 1
		self.paid = False
		print('Watched Successfully!!')


	def _payment_transaction(self):

		payment = int(input('payment: '))
		if self.movie_amount == payment:
			self.paid = True
			print('Transaction done!! You can watch the movie now')
		elif self.movie_amount < payment:
			self.paid = True
			change = payment - self.movie_amount
			print(f'Transaction done!! You have a change worth of {change}')
		else:
			print('Your payment is not enough')



watch = movie_world()
watch.play_movie()


