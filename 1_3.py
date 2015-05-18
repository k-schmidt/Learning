'''
Write a short Python function, minmax(data), that takes a sequence 
of one or more numbers, and returns the smallest and largest numbers, 
in the form of a tuple of length two. 
Do not use the built-in functions min or max in implementing your solution.
'''

def minmax(data):
    biggest = data[0]
    smallest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
	if val < biggest:
	    smallest = val
	print (biggest, smallest)

if __name__ == '__main__':
    minmax([2,4,6,8,10])
    minmax([3,2,6,20,4,7])
