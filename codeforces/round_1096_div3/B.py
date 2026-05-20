# https://codeforces.com/contest/2227/problem/B
def solve():
	for _ in range(int(input())):
		_ = input()
		s = input()
		# cannot be correct bracket sequence
		if len(s) % 2 == 1:
			print("NO")
			continue
		lcount = s.count("(")
		print("YES" if lcount == len(s)//2 else "NO")
solve()