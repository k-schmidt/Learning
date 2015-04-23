'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(a):
    return all(a % i for i in xrange(2, a))

def prime_factor(number):
	L = []
	for x in xrange(1, number):
		if number % x == 0: 
			for i in xrange(2, x):
				if x % i != 0:
					L.append(x)
		else:
			next
	return max(L)

print is_prime(600851475143)
print prime_factor(600851475143)
