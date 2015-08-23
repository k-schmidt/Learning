'''
Write a short Python function that takes a sequence of integer values and 
determines if there is a distinct pair of numbers in the sequence whose 
product is odd.
'''

def unique_set(data):
	return set(data)

#Must call data ahead of time
data = [66,77,88,99,100,102]
s = set(data)

def find_odds(set):
	print [x for x in set if x % 2 != 0] 
	return [x for x in set if x % 2 != 0]

if __name__ == '__main__':
	find_odds(unique_set([1,2,2,3,3,5,5,6,6,9,9,10]))
	find_odds(s)
