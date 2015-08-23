'''
Demonstrate how to use Python's list comprehension syntax to produce the list 
[1, 2, 4, 8, 16, 32, 64, 128, 256].
'''

def list_comp(data):
	power_of_two = [2 ** x for x in xrange(len(data))]
	print power_of_two
	return power_of_two

def list_comprehension_example():
	print [pow(2,x) for x in range(9)]
	return [pow(2,x) for x in range(9)]

if __name__ == '__main__':
	list_comp(range(9))
	list_comprehension_example()
