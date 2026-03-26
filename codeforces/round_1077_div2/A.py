# https://codeforces.com/contest/2188/problem/A

# okay, I need to think of this like jumps on a number line
# 2
# 2 1
# 3
# 1 2 3
# 2 3 1
# 4
# 1 2 3 4
# 2 3 1 4
# 5
# 1 2 3 4 5
# Ah start at the middle and ping pong back and forth across the pivot

def solve():
	for _ in range(int(input())):
		n = (int(input()))
		res = []
		current = n // 2 + n % 2
		res.append(current)
		for i in range(1,n):
			if i % 2 == 1:
				current += i
			else:
				current -= i
			res.append(current)
		print(*res)
solve()