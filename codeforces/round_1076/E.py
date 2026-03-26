def solve():
	for _ in range(int(input())):
		n = int(input())
		a = list(map(int,input().split()))
		elements = sorted(list(set(a)))
		# considering dp[i,j] best way to reach j given the first i elements
		dp = [[float('inf') for _ in range(n+1)] for _ in range(len(elements)+1)]
		dp[0][0] = 0
		for i in range(1,len(elements)+1):
			for j in range(n+1):
				divisors = [1]
				factor = elements[i-1]
				while factor <= j:
					divisors.append(factor)
					factor *= factor
				# Check all possible powers of factor d <= j
				print(i)
				dp[i][j] = min(dp[i-1][j//d] + i if j % d == 0 else float('inf') for i,d in enumerate(divisors))
		res = [-1 for _ in range(n)]
		for i in range(1,n+1):
			if dp[len(elements)][i] != float('inf'):
				res[i] = dp[i-1][i]
		print(*res)
solve()