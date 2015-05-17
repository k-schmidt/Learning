'''
Write a short Python function, is_multiple(n, m), that takes two integer values 
and returns True if n is a multiple of m, that is, n = mi for some integer i,
and False otherwise.
'''

def is_multiple(n, m):
    try:
        return True if (int(n) % int(m) == 0) else False
    except ValueError:
        print "Numbers must be Integer values"

if __name__ == '__main__':
    is_multiple(50,3)
    is_multiple(2,50)
    is_multiple(50,2)
