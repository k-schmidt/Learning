'''
Write a short Python function that takes a positive integer n and returns the 
sum of the squares of all the positive integers smaller than n.
'''

def sum_squares(k):
	sum = 0
	try:
		for x in range(k,0,-1):
			square = x**2
			sum += square
		print sum
	except TypeError:
		print("Input object is not an integer")


if __name__ == '__main__':
	sum_squares(10)
	sum_squares('Radio')
	sum_squares([2, 4, 6, 8])
	k =10
	sum_squares = sum([pow(x,2) for x in range(k,0,-1)])
	print sum_squares
