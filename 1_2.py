'''
Write a short Python function, is_even(k), that takes an integer value 
and returns True if k is even, and False otherwise. 
However, your function cannot use the multiplication, modulo, or division operators.
'''

def is_even(k):
    try:
	return True if int(k) & 1 == 0 else False
    except ValueError:
	print "Number must be Integer values"

if __name__ == '__main__':
    is_even(10)
    is_even(12)
    is_even(13)
