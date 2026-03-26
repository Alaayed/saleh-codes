MOD = 1000000007
def sol():
	n = int(input())
	for _ in range(n):
		d = int(input())
		print((8*pow(9 , d-1 , MOD) % MOD))
sol()

