"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
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
p = prime_upto(200000)
print(len(p))
print(p[10000])   # 10001 prime
#print(p[:100])


"""
Printed p[10001] , forgot that index starts from 0. xD
"""