def solve():
	nums = list(map(int, input().split()))
	res = nums[-1] % 10
	if res == 0: 
		res = 10
	print(res)
solve()
