def _sum(x):
	y = 0
	for i in x:
		y += i
	print y

def _sum_string(x):
	for i in x:
		y += i
	print y

if __name__ == '__main__':
	_sum([1,2,3,4,5])
	_sum_string(["hello","goodbye"])
