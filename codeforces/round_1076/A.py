def solve():
	t = int(input())
	for _ in range(t):
		n,s,x = map(int, input().split())
		nums = list(map(int, input().split()))
		current_sum = sum(nums)
		# Fail condition, can subtract
		if current_sum > s:
			print('NO')
			continue
		# difference is a multiple of x
		if (s-current_sum) % x == 0:
			print('YES')
		else:
			print('NO')
solve()