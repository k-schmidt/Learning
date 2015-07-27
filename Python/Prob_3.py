'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime_factor(x,n):
    L=[2]
    if x < n:
        if n % x == 0:
            if any(x % i == 0 for i in L):
                prime_factor(x + 1, n)
            else:
                L.append(x)
                print L
                prime_factor(x + 1, n)
        else:
            prime_factor(x + 1, n)
    else:
        print "{0} is greater than {1}.".format(x,n)

if __name__ == '__main__':
	prime_factor(2,100)
