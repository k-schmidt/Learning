'''
What parameters should be sent to the range constructor, to produce a range 
with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
'''

def origin_range():
	range_around_origin = [x for x in xrange(8, -9, -2)]
	print range_around_origin

def range_from_eigth():
	print range(8,-9,-2)
	return range(8,-9,-2)

if __name__ == '__main__':
	origin_range()
	range_from_eigth()
