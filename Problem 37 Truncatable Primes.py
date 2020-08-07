"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def b_search(l, key):    # binary search
	low = 0
	high = len(l)-1
	while(low<=high):
		mid = low + (high - low)//2
		if(l[mid]==key):
			return True
		elif(l[mid]<key):
			low = mid + 1
		else:
			high = mid - 1
	return False

def left_t(n,primes):
	if(n in [2,3,5,7]):
		return True
	n=n//10
	if(b_search(primes,n)==True):
		return left_t(n, primes)
	else:
		return False

def right_t(n,primes):
	if(n in [2,3,5,7]):
		return True
	n=int(str(n)[1:])
	if(b_search(primes,n)==True):
		return right_t(n, primes)
	else:
		return False

def solve():
	primes = prime_upto(1000000)
	ans = []
	for prime in primes:
		if(prime>10):
			both = 0
			if(left_t(prime,primes)==True):
				#print(prime, "L")
				both +=1
			if(right_t(prime,primes)==True):
				#print(prime, "R")
				both +=1
			if(both == 2):
				ans.append(prime)
				print(prime, "I AM HERE")
	print(ans)
	print(sum(ans))




def solve2():
	primes = prime_upto(10000)
	plr = [2,3,5,7]
	p0 = [2,3,5,7]

				
solve()