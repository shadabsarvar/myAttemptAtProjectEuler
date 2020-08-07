"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import math
def open_file():
	with open("p099_base_exp.txt",'r') as f:
		s = f.read()
	return s

def process_input(s):
	l=s.split("\n")
	#print(l)
	ll = []
	for i in l:
		ll.append(list(map(int,i.split(','))))
	return ll

def solve():
	s = open_file()
	l = process_input(s)
	#print(l)

	n = len(l)
	ans = 0
	ans_i = 0
	for i in range(n):
		A, B = l[i]
		BlogA = B* math.log(A)
		if(BlogA > ans):
			ans = BlogA
			ans_i = i
	print(ans_i+1)

solve()