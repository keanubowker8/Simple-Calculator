def add(*args):
	'''takes any amount of numbers passed and adds them'''
	sum = 0
	for number in args:
		sum += number
	return sum


def multiply(*args):
	'''takes any amount of numbers passed and multiplies them'''
	sum = 1
	for number in args:
		sum *= number
	return sum	