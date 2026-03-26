# link: https://codeforces.com/group/xSQ0pfWy2O/contest/674999/problem/A

def solve_test_case():
	n = int(input())
	arr = list(map(int, input().split()))
	total_odd = 0
	odd_prefix_count = [total_odd := total_odd + (1 if arr[i] %2 == 1 else 0) for i in range(n)]
	total_sum = 0
	prefix_sum = [total_sum := total_sum + arr[i] for i in range(n)]
	result= [arr[0]]
	for i in range(1,n):
		olay_turns = odd_prefix_count[i] // 3
		remaining_odd = odd_prefix_count[i] % 3
		if remaining_odd == 1: olay_turns += 1
		result.append(prefix_sum[i] - olay_turns)
	print(*result)

def solve():
	test_cases = int(input())
	for _ in range(test_cases):
		solve_test_case()

solve()