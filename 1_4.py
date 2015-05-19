'''
Write a short Python function that takes a positive integer n and returns the 
sum of the squares of all the positive integers smaller than n.
'''

def smaller_squares(k):
	sum = 0
	for x in range(k,0,-1):
		square = x**2
		sum += square
	print sum

if __name__ == '__main__':
	smaller_squares(10)
