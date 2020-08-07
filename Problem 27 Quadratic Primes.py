"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
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

def quad(a,b,n):
	return (n*n + a*n + b) 

def isPrime(primes,p): # primes is list of primes , p is number to be checked
	if(p>primes[-1]*primes[-1]):
		print("Error: prime list is small", p, primes[-1])
	else:
		if (p <primes[-1]):
			if (p in primes):
				return True
			else:
				return False
		else:
			for prime in primes:
				if(p%prime!=0):
					return False
			return True


def solve():
	N = 10000			# hit and trial
	primes = prime_upto(N)
	ans = [0,0,0]  # a,b,n
	for a in range(-1000,1001):
		for b in range(-1000,1001):
			for n in range(100000):
				e = quad(a, b, n)
				if(isPrime(primes,e)==True):
					if(ans[2]<n):
						ans = [a,b,n]
						print(ans)
				else:
					break
	print(ans)

solve()
print(-61*971)