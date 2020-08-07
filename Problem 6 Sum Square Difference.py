"""
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_square_diff(n):
	ans =( n * (n+1) * (3*n*n-n-2))//12
	return ans
print(sum_square_diff(10))
print(sum_square_diff(100))