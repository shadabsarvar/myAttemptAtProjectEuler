"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def list_digit(n): # return digits of n as list
	l = []
	while(n>0):
		l.append(n%10)
		n//=10
	return(l[::-1])

def fac10(n): # generates factorial upto n and returns the list
	l=[1,1]
	for i in range(2,n+1):
		l.append(i*l[-1])
	return(l)


def solve(n):
	fac = fac10(10)
	ans = []
	for i in range(10,n):
		s = list_digit(i)
		sum_dig = sum(fac[i] for i in s)
		if sum_dig == i:
			ans.append(i)
			print(i,sum(ans))
			
	return(ans)
a = solve(100000)
print(a)
print(sum(a))
