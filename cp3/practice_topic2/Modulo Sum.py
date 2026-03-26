# https://codeforces.com/problemset/problem/577/B

# Almost CERTAINLY some form of DP with one of the states being M
# Ain't no way the bound on m is 1000 for no reason
# Something like dp[cur][j] where the state is;
# Given the first cur elements, is it possible to reach  (some sum) % j == m
# Transition would be dp[cur][j]= max(dp[cur-1][j], dp[cur-1][(j+num[cur])% m], dp[cur][j])
# base cases: dp[i][nums[i] % m] = 1
# We visit each state at most once
# |S| = 10^6 * 10^3 = 10^9
# it's within bounds

# First submit

# submitted, crashed on test 16 from memory limit failure
# Ah, just realized that was a gigabyte of data the states were storing.
# If you imagine it as a column, I just need two columns.
# The "current" column--the one thats being updated-- and the previous one.
# still 10^9 computations but only 2000 states tracked
# could probably use a python style swap function for fast swaps

# second submit

# TLE on test 16. The swaps just aren't fast enough.
# I will try reimplementing in c++ to see if that fixes it

# Third attempt

# Turns out that for any value n > m the answer is always yes duo to the pigeonhole principle
# Case 1: there exists some prefix sum S_i mod m == 0:
# Just return YES
# Case 2: There does not exist any prefix sum S mod m == 0:
# By the pigeonhole principle there must exist some i,j s.t. (S_i == S_j) mod m
# There for S_i - S_j == 0 mod m
# Or more concretely, a_i + a_{i+1} ... a_j == 0 mod m
def solve():
	n,m = map(int, input().split())
	# make nums 1 indexed, for simplicity and uniformity
	nums = [0] + list(map(int, input().split()))
	if (n > m):
		print('YES')
		return None
	current  = [0 for _ in range(m)]
	for i in range(1, n+1):
		previous = current
		current = [0 for _ in range(m)]
		for j in range(0, m):
			current[j] = max(previous[j] , previous[(j - nums[i])% m], (nums[i]%m) == j)
	print('YES' if current[0]  else 'NO')
solve()