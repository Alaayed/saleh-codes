BOUND = int(1e9+7)
# https://cp-algorithms.com/algebra/factorial-modulo.html
f=[]
def precompute_fact_mod(p):
	f.append(1)
	for i in range(1,(10**6) + 1):
		f.append( f[i-1] * i % p)
def fact_mod(n , p):
	res = 1
	while (n > 1):
		if (n/p % 2 == 1):
			res = p - res
		res = res * f[n] % p
		n /= p 
	return res 
def choose(n, i):
	if (n<= 0):
		return 0
	elif (i > n):
		return 0
	elif(n == 1):
		return 1
	return int(fact_mod(n, BOUND) * pow((fact_mod(n-i, BOUND) * fact_mod(i, BOUND)),-1, BOUND))
def hopscotch():
	(n , x , y) = map(int , input().split())
	precompute_fact_mod(BOUND)
	paths = 1
	for i in range(1 , n):
		xc = choose (n-(x-1)*(i+1) -1, i )
		yc = choose (n-(y-1)*(i+1) -1, i )
		paths = (paths + xc * yc) % BOUND
	print(int(paths))
hopscotch()
