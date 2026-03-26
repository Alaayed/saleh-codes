BOUND = int(1e9+7)
f=[]
def precompute_fact_mod(p):
        f.append(1)
        for i in range(1,(2500) + 1):
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
def colors():
	precompute_fact_mod(BOUND)
	(n, c) = map(int , input().split())
	colorings = (c * pow( (c-1), n -1 , BOUND) ) % BOUND
	num = 0
	for i in range(1 , c):
		ways = choose(c,i)
		valid_colorings = (c-i) * pow(c-i-1 , n-1 , BOUND)
		term = ways * valid_colorings * (-1) ** (i-1)
		num =(num + term) % BOUND
	res = colorings-num
	res = max(res, (res+ BOUND) % BOUND)
	print(colorings-num)
colors()
