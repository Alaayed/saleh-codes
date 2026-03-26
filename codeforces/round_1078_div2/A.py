# link: https://codeforces.com/contest/2194/problem/A
def solve():
	for _ in range(int(input())):
		n, w = map(int, input().split())
		print(n - n // w)
solve()