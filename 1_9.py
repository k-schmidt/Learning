'''
What parameters should be sent to the range constructor, to produce a range 
with values 50, 60, 70, 80?
'''

def range_from_fifty():
	return range(50,81,10)

if __name__ == '__main__':
	range_from_fifty()
	list = [x for x in xrange(50,81,10)]
	print list
