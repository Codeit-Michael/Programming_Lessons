def add_time(base_time,duration,day = None):
	Fleft,Fright = base_time.split(':')
	Sleft,Sright = duration.split(':')
	Fright,Base = Fright.split(' ')

	ampm_selector = ''
	ampm = {'PM':'AM','AM':'PM'}
	weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	days_later = 0
	add_day = int(Sleft)
	next_days = 0

	left_main = int(Fleft) + int(Sleft)
	right_main = int(Fright) + int(Sright)
	while right_main >= 60:
		right_main -= 60
		left_main += 1
	if len(str(right_main)) == 1: right_main = f'0{right_main}'

	while left_main >= 12:
		if add_day >= 24:
			add_day -= 24
			days_later += 1
		left_main -= 12
		ampm_selector = ampm[Base]
		Base = ampm_selector
		if Base == 'AM':
			next_days += 1
	if len(str(left_main)) == 1:
		if left_main == 0:
			left_main = 12
		else:
			left_main = f'0{left_main}'

	new_time = f'{left_main}:{right_main} {Base}'

	if days_later != 0: new_time += f', {days_later}day/s later'

	if day != None:
		new_index = next_days + weekdays.index(day)
		while new_index > len(weekdays): new_index -= len(weekdays)
		new_time += f', {weekdays[new_index]}'
	return new_time

if __name__ == '__main__':
	print(add_time("11:43 PM", "24:20", "Tuesday"))
	print(add_time("6:30 PM", "205:12"))
