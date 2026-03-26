import math
UPPERBOUND = 10**9+1
def is_coprime(k,c):
	return math.gcd(k,c) == 1
def solve_candy(k,c):
	if not is_coprime(k,c):
		print("IMPOSSIBLE")
		return None
	solution = pow(c,-1,k)
	if solution >= UPPERBOUND:
		print("IMPOSSIBLEE")
		return None
	print(solution)
def candy_dis():
	n = int(input())
	for _ in range(n):
		k,c = map(int,input().split())
		solve_candy(k,c)
candy_dis()
