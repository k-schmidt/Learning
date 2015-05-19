'''
Write a short Python function that takes a positive integer n and returns the 
sum of the squares of all the odd positive integers smaller than n.
'''

def sum_of_odd_integers(n):
	print sum([pow(x, 2) for x in xrange(1,n,2)]) if n > 0 else False
	return sum([pow(x, 2) for x in xrange(1,n,2)]) if n > 0 else False


if __name__ == '__main__':
	sum_of_odd_integers(100)
