# link: https://codeforces.com/group/xSQ0pfWy2O/contest/670998/problem/C
MAXN = 1000 + 5
MAXK = MAXN * 2 + 5
UNCONTESTED = 0
CONTESTED = 1
MOD = 998244353
dp = [
		[
		[0,0] for _ in range(MAXK)
        ] for _ in range(MAXN + 1)]
def push_dp(n,k):
	# Contested endings can NOT increase the number of components
	# ALl new ways to add components result in k components
	# Handle all contributions of dp[n][k][UNCONTESTED]
	# Case 1, simple extension
	dp[n+1][k][UNCONTESTED] += dp[n][k][UNCONTESTED]
	# Case 2, color inversion
	dp[n+1][k+1][UNCONTESTED] += dp[n][k][UNCONTESTED]
	# Case 3, color contest
	dp[n+1][k+1][CONTESTED] += 2*dp[n][k][UNCONTESTED]
	# Handle all contributions of dp[n][k][CONTESTED]
	# Case 1, simple extension
	dp[n+1][k][CONTESTED] += dp[n][k][CONTESTED]
	# Case 2, Color inversion
	dp[n+1][k+2][CONTESTED] += dp[n][k][CONTESTED]
	# Case 3, solid color
	dp[n+1][k][UNCONTESTED] += 2*dp[n][k][CONTESTED]
	for i in range(0,3):
		for j in range(0,2):
			dp[n+1][k+i][j] %= MOD

def solve():
	n,k = map(int,input().split())
	# base case
	dp[1][1][UNCONTESTED] = 2
	dp[1][2][CONTESTED] = 2
	for i in range(1,n+1):
		for j in range(1,2*n +1):
			push_dp(i,j)
	print( ( dp[n][k][UNCONTESTED] + dp[n][k][CONTESTED]) % MOD)
solve()