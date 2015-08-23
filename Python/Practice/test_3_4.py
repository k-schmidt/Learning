def do_twice(f,bruce):
	f(bruce)
	f(bruce)

def print_spam(spam):
	print spam

def do_four(f,bruce):
	f(print_spam, bruce)
	f(print_spam, bruce)

if __name__ == '__main__':
	do_four(do_twice, 'bruce')
