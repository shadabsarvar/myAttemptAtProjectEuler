"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

ans = 0 
t10 = pow(10, 10)
for i in range(1,1001):
	ans += pow(i, i,t10)
print(ans)
print(ans%t10)