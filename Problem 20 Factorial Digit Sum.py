"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)

def sum_digit(n):
	sumDigit = 0
	while(n>0):
		sumDigit += n%10
		n//=10
	return(sumDigit)
n=100
print(sum_digit(factorial(n)))