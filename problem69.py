import eratosthenes.eratosthenes as es

def divisors(n):
	'''
	Returns a tuple of all numbers that divide n, including 1 and n.
	Ex. divisors(12) = [1,2,3,4,6,12]

	'''

	l = []

	for x in range(1,n + 1):
		if n % x == 0:
			l.append(x)

	return l

def rp(n):
	'''
	Returns a tuple of all numbers relatively prime to n.
	Ex. rp(12) = [1,5,7,11]

	'''

	if es.prime(n): # n itself is prime:
		# protip: If a number is prime, then all numbers up to n
		# are relatively prime to n.
		# ex. rp(7) = (1,2,3,4,5,6)

		return tuple(range(1,n))

	


