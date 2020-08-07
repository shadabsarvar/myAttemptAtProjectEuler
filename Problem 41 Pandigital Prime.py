"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools
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

def isPandigital(n):
	if(len(list(str(n)))==len(set(list(str(n)))-set("0"))):
		return True
	else:
		return False


def check_prime(m,p):
	#n = int(m**(0.5))        
	#p = prime_upto(n)
	#print(p[-1])
	for pr in p:
		#print(pr,m)
		if m%pr == 0:
			return pr
	return 1


def gen_9digit_pandigital():
	l = [1,2,3,4,5,6,7]
	n = list(itertools.permutations(l))
	k = []
	for i in n:
		k.append(int(''.join( str(j) for j in i)))
	return k


def solve():
	p = prime_upto(10000000)
	for pi in p:
		if isPandigital(pi):
			ans = pi
	print(ans)


def solve2():
	p = prime_upto(100000)
	#print(p[-1])
	l = gen_9digit_pandigital()
	l.sort()
	l = l[::-1]
	#print(l)
	print(check_prime(98765431,p))
	for i in l:
		#print(i,check_prime(i,p))
		if(check_prime(i,p)==1):
			print(i)
												
solve()
solve2()