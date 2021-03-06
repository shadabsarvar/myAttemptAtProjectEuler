"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def list_digit(n): # return digits of n as list
	l = []
	while(n>0):
		l.append(n%10)
		n//=10
	return(l[::-1])
def sum_pow5(l):
	return(sum((i**5) for i in l))
def solve():
	s = []
	for i in range(10,1000000):
		sd=sum_pow5(list_digit(i))
		#print(i,sd)
		if i == sd:
			s.append(i)
	print(s)
	print(sum(s))

solve()