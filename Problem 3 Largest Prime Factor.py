"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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


def largest_prime_factor(m):
	n = int(m**(0.5))        
	p = prime_upto(n)

	lpf = 1
	for pr  in p:
		while(m%pr == 0):
			#print(m,pr)
			m=m//pr

			lpf = pr
	if m !=1:
		lpf = m
	#print(p)
	return lpf


print(largest_prime_factor(600851475143))
