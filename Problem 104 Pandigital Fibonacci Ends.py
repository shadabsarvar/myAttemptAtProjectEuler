"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""

"""def gen_fibo(n,a = 1, b = 1):
	fibo = [a,b]
	for i in range(n-2):
		fibo.append(fibo[-1]+fibo[-2])
	return fibo

def gen_set_1_to_9():
	s = "123456789"
	return(set(s))
"""
def len_int(n):
	return(len(str(n)))

def check_1_to_9(n, ch,i):
	#print(n, ch)
	l = [0]*10
	l1 = [1]*10
	l1[0]=0
	n = str(n)
	if (ch == 1):
		n = n[:9]
	elif(ch == -1):
		n = n[-9:]
	ln = len(n)
	for i in range(ln):
		l[int(n[i])]+=1

	if(i == 2749 -3 ):
		print(l,l1)
	if (l==l1):
		"""print(n)
								print(l)
								print(l1)"""
		return True
	else:
		return False


def solve():
	N =1000000
	f1=f1f=1
	f2=f2f=1
	###set_1_to_9 = gen_set_1_to_9()
	for i in range(N):
		fn = f1 + f2
		f2 = f1
		f1 = fn
		
		fnf = f1f + f2f
		f2f = f1f						## forgot to update these
		f1f = fnf						## f1f and f2f were not reducing

		fn %=  1000000000

		"""if(str(fn)[:10]!=str(fnf)[:10]):
									print(i,fnf,str(fn)[:13])
									break
								"""
		
		fnf = str(fnf)
		lfnf = len(fnf)
		if(len(fnf)>20):
			d = lfnf - 20
			fnf = int(fnf[:-d])
			f1f = int(str(f1f)[:-d])
			f2f = int(str(f2f)[:-d])
			
		if len_int(fn)>=9 or len_int(fnf)>=9:
			#print(i, fn)
			#break
			
			both = 0
			if(check_1_to_9(fnf,1,i)== True):
				print(i+3,'F')
				#rint(fnf)
				both +=1
			if(check_1_to_9(fn,-1,i)== True):
				print(i+3,'B')
				#print(fn)
				both +=1
			if(both==2 ):
				print("Found")
				break

			"""
			set_beg = set(str(fnf)[:9])
			set_end = set(str(fn)[-9:])
			if(i == 100):
				print(fn)
				print(set_beg, set_end)
				print(set_1_to_9)
			if (set_beg == set_1_to_9):
				print(i+3,'F')
				print(fnf)
			if (set_end == set_1_to_9):
				print(i+3,'B')
				print(fn)
			if (set_beg == set_1_to_9 and set_end == set_1_to_9):
				print(i+3)
				print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
				break
			"""
solve()


## TOOK >3 hrs to debug this 
## Got back the spark of programming