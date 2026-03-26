# https://codeforces.com/contest/2184/problem/C
# I dont want to think too much, ill just do dfs. it cant be that bad
memo = {}
def dfs(cur, k, divs):
	if cur in memo: return memo[cur]
	if cur == k:
		memo[cur] = divs
		return memo[cur]
	if cur < k:
		memo[cur] = float('inf')
		return float('inf')
	memo[cur] = min(dfs(cur // 2, k , divs+1) , dfs(cur // 2 + cur % 2, k , divs+1))
	return memo[cur]

def solve():
	for _ in range(int(input())):
		n,k= map(int,input().split())
		val = dfs(n,k,0)
		print(val if val != float('inf') else -1)
		memo.clear()

solve()