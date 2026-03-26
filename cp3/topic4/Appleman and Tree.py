# link: https://codeforces.com/group/xSQ0pfWy2O/contest/670998/problem/B

# Really enjoyed working through this problem.
# Count the number of ways for children to white or black
# Gives you the number of ways you can be black or white
# Use a recursive definition
# Answer is just the number of ways the root can be part of a black set

# More concretely, dp(child) return B,W.
# B = # subsets where child is solved (i.e. obeys the constraints of the problem)
# W = # connected sets where the child is white and everything not part of the childs subset is black
# special case: if we are black,
# Ah, just keep a running tall since each child is an independent event
# B` = B * B_C + B*W_C + B_C*W
# W` = W*W_C + B_C * W
mod = 10**9 + 7
MAXN = 10**5 + 5
adj   = [[] for _ in range(MAXN)]
parent = []
results = [[0,0] for _ in range(MAXN)]
def is_black(child):
	return black[child] == 1
def iterative_dp(root):
	stack = [c for c in adj[root]]
	order  = []
	while stack:
		node = stack.pop()
		order.append(node)
		for child in adj[node]:
			stack.append(child)
	for node in reversed(order):
		pn = parent[node]
		b,w,bc,wc = results[pn][0], results[pn][1], results[node][0], results[node][1]
		b = (b * bc + b * wc + bc * w) % mod
		w = (w * wc + w * bc) % mod
		results[pn][0] = b
		results[pn][1] = w
def dp(parent):
	w,b = 0,0
	if is_black(parent): #
		b=1
	else:
		w=1
	for child in adj[parent]:
		bc, wc = dp(child)
		b = (b*bc + b*wc + bc*w) % mod
		w = (w*wc + w*bc) % mod
	return b,w

def solve():
	n = int(input())

	global black, parent, results
	parent = list(map(int, input().split()))
	for child,p in enumerate(parent):
		adj[p].append(child+1)
	black = list(map(int, input().split()))
	for i,b in enumerate(black):
		results[i][0] = 1 if b == 1 else 0
		results[i][1] = 1 if b == 0 else 0

	parent = [0] + parent
	iterative_dp(0)
	print(results[0][0])

solve()