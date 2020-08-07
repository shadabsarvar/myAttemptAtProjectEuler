"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


n = pow(2, 1000)


sumDigit = 0
print(n)
while(n>0):
	sumDigit += n%10
	n//=10
print(sumDigit)

# Also # Another method
n = pow(2, 1000)
sumDigit = sum(int(i) for i in str(n))
print(sumDigit)
## Python does calculate 2**1000 fast :D
