"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def solve():
	for i in range(1,1000000):
		l = []
		for j in range(1,7):
			l.append(set(str(i*j)))
		ans = True
		for j in range(1,6):
			if (l[j]!=l[0]):
				ans = False
		if (ans == True ):
			print(i)

solve()