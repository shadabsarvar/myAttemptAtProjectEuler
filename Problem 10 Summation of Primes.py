"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sieve_e(n): # Generate sieve of erathosthenes for n numbers
	# 1 = prime
	# 2 = composite
	a =[0]*(n+1)    
	for i in range(2,n):
		if (a[i]==0):
			a[i]=1        # Marked prime
			for j in range(i*2,n,i):      # All the multiples of i
				a[j]=2		# Marked Composite
	return a

def prime_upto(n):  # Returns all primes less than n
	a = sieve_e(n)
	p = []
	for i in range(n):
		if a[i]==1:
			p.append(i)
	return(p)

primes = prime_upto(2000000)
print(sum(primes))