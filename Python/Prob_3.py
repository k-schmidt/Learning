'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def sieve(x):
    large_prime = 2
    while x > large_prime:
        if x % large_prime == 0:
            x = x / large_prime
            large_prime = 2
        else:
            large_prime += 1
    print "Largest Prime Factor: {0}".format(large_prime)

if __name__ == '__main__':
	sieve(600851475143)
