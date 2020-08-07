"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
import math
def solve():
	ans = 0
	for a in range(1,100):
		x = pow(10, 1 + 1/a)
		x = 10 
		y = pow(10, 1 + 1/a)
		print(a,x,y)
		ans+= int(y-x)
	print(ans)

solve()