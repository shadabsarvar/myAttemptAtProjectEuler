"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Simpifying a+b+c = 1000 and (a+b)^2 =c^2 gives
ab = 1000(a+b =500)    Eq 1
"""

def solve():
	for a in range(500):
		for b in range(500):
			exp_r =  1000*(a+b-500)
			if(a*b == exp_r):
				return(a,b,1000-a-b)

def verify(a,b,c):
	print(a*a + b*b, c*c)

a,b,c = solve()
print(a,b,c)
print(a*b*c)
verify(a, b, c)