'''
Python's random module includes a function choice(data) that returns a random 
element from a non-empty sequence. The random module includes a more basic 
function randrange, with parameterization similar to the built-in range 
function, that return a random choice from the given range. Using only the 
randrange function, implement your own version of the choice function.
'''

def choice_test(data):
	import random
	print data[random.randrange(0, len(data))]
	return data[random.randrange(0, len(data))]

if __name__ == '__main__':
	choice_test([1,5,6,7,21,30,33,4,11,2])
