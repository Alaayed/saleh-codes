# https://codeforces.com/contest/2184/problem/B

def solve():
	for _ in range(int(input())):
		s,k,m = map(int,input().split())
		flip = m // k
		# Easy case
		if flip == 0:
			print(max(0, s-m))
			continue
		# if it's odd, there was min(s,k) in the hourglass
		if flip % 2 == 1:
			print(max(min(s,k) - m % k, 0))
		else:
			# s= 4 k = 8 m = 17
			# s= 100, k= 8 m = 17
			print(max(s - m % k,0))
solve()
# 92 / 8
# 8  / 92
# 0 / 100
# 100/0