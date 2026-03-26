from math import comb
def solve():
	(n,k) = map(int, input().split())
	diff = set()
	for _ in range(n):
		j = int(input())
		diff.add(j)
	num_diff = len(diff)
	print(min(k, num_diff))
solve()
