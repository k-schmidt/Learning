'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(a):
    if all(a % i for i in xrange(2, a)):
		return a

def list_primes(n):
	A = [True] * n 
	for i in xrange(2, n**(0.5) + 1,2):
		if A[i]:
			A[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if A[i]]


if __name__ == '__main__':
	list_primes(600851475143)
