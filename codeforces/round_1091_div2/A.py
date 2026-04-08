#link : https://codeforces.com/contest/2217/problem/A

def solve():
	t = int(input())
	for _ in range(t):
		n,k = map(int,input().split())
		a = list(map(int,input().split()))
		sa = sum(a)
		if sa % 2 == 1 or n*k % 2 == 0: print('YES')
		else: print('NO')



solve()