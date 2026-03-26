# https://codeforces.com/contest/2184/problem/A
def solve():
	n = int(input())
	if n == 2 or n == 3:
		print(n)
	else:
		print(n % 2)

def tsolve():
	t= int(input())
	for i in range(t):
		solve()
tsolve()