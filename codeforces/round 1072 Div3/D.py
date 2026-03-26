# https://codeforces.com/contest/2184/problem/D'
# dp[i] assuming i bits are set,how many invalid ways exist
# dp[i][j] same, but the last bit is set at j
from math import comb
def solve():
	for _ in range(int(input())):
		n,k = map(int,input().split())
		dp = [[0 for _ in range(31)] for _ in range(31)]
		res = 0
		msb_pos = n.bit_length() - 1
		msb_bit = (n >> msb_pos) & 1
		for i in range(31):
			for j in range(1,msb_pos):
				dp[i][j] = comb(j-1,i) if (i+j) > k else 0
				res += dp[i][j]
		print(res)
solve()