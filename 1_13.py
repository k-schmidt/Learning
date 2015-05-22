'''
Write a pseudo-code description of a function that reverses a list of n 
integers, so that the numbers are listed in the opposite order than they were 
before, and compare this method to an equivalent Python function for doing the 
same thing.
'''

def reverse(data):
	reversed_list = [k-(len(data))-1 for k in xrange(1,len(data)+1)]
	print reversed_list

def other_reverse(data):
	print data[::-1]

def standard_reverse(data):
	return reversed(data)

if __name__ == '__main__':
	reverse([1,2,3,4,5])
	other_reverse([1,2,3,4,5])
