def separator():
	print '+', 4 * '-', '+', 4 * '-', '+'

def body():
	print '|', 4 * ' ', '|', 4 * ' ', '|'

def do_four(x):
	x()
	x()
	x()
	x()

def grid(f,g,h):
	f()
	h(g())
	f()
	h(g())

grid(separator,body,do_four)
