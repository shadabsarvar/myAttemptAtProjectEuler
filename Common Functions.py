## Prime numbers

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
		print(low,mid, high,'b')
		if(l[mid]==key):
			return mid
		elif(l[mid]<key):
			low = mid + 1
		else:
			high = mid - 1
		print(low,mid, high)
	return -1

print(b_search([23,454,23423,234234234,232212324,35345345345345], 35345345345345))
