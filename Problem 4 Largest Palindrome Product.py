"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(n):
	n = str(n)
	r = n[::-1]
	if (r == n):
		return True
	else:
		return False
def largest_palindromic_product():
	lpp = 1
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			p = i*j
			if is_palindrome(p):
				if lpp<p:
					lpp = p
			if lpp>p:
				continue
	return(lpp)

print(largest_palindromic_product())