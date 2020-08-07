"""
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
"""


def sum_digit(n):
	sumDigit = 0
	while(n>0):
		sumDigit += n%10
		n//=10
	return(sumDigit)

def solve():
	ans = 0
	A,B = 0, 0
	for a in range(1,100):
		for b in range(1,100):
			s = sum_digit(pow(a,b))
			if(s>ans):
				ans = s
				A = a
				B = b
	print(ans)
	print(A,B,A**B)

solve()