import math 
def mag():
	(n,k,p) = map(int , input().split())
	lb = math.ceil(n/p)
	ub = k
	picograms = []
	for i in range(1 , math.ceil(math.sqrt(n))):
		divides = (n % i) == 0
		if divides: 
			d1 = n // i
			if (d1 >= lb and d1 <= k):
				picograms.append(d1)
			if (i >= lb and i <= k):
				picograms.append(i)
	root = math.sqrt(n)
	divides = (n % root) == 0
	if divides and (root >= lb and root <= k):
		picograms.append(int(root))
	picograms.sort()
	print(len(picograms))
	list(map(print , picograms))
mag()
