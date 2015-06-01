'''
Write a Python function that takes a sequence of numbers and determines if 
all the numbers are different from each other (that is, they are distinct).
'''

def is_unique(data):
	if len(set(data)) < len(data):
		print "Numbers are not distinct"
	else:
		print "Numbers are distinct"

def check_if_unique(data):
	s = set(data)
	print len(s) == len(data)
	return len(s) == len(data)

if __name__ == '__main__':
	is_unique([1,2,3,2,3,4,5,3,5])
	check_if_unique([1,2,3,2,3,4,5,3,5])
