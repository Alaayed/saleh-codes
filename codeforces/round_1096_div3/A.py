# https://codeforces.com/contest/2227/problem/A
def solve():
	for _ in range(int(input())):
		x,y = map(int, input().split())
		if x%2==1 and y%2==1: print("NO")
		else: print("YES")

solve()