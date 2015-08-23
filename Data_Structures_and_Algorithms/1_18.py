'''
Demonstrate how to use Python's list comprehension syntax to produce the list 
[0,2,6,12,20,30,42,56,72,90].
'''

def list_comp():
	print [index * x for index, x in enumerate(range(1,11))]

if __name__ == '__main__':
	list_comp()
