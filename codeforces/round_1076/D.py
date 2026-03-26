def solve():
	for _ in range(int(input())):
		n = int(input())
		a = list(map(int,input().split()))
		b = list(map(int,input().split()))
		t = 0
		# Get prefix sum
		psumB = [ t:= i+t for i in b]
		a.sort()
		# dp[i] maximum score to pass level i
		dp = [0] + [ (a[-psumB[i]] if psumB[i] <= n else 0) * (i+1) for i in range(n)]
		print(max(dp))
solve()