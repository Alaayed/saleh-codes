# link: https://codeforces.com/group/xSQ0pfWy2O/contest/674999/problem/C
import numpy as np
from collections import deque, Counter
from fractions import Fraction


def mex(a):
	if not a: return 0
	i = 0
	while i < len(a) and a[i] == i:
		i += 1
	return i


def compute_grundy_numbers(dg, outdegrees):
	grundy = [-1 for i in range(len(dg))]
	# start from leaves
	rdg = [[] for _ in range(len(dg))]
	for parent in range(len(dg)):
		for child in dg[parent]:
			rdg[child].append(parent)
	# from sinks
	queue = deque(i for i in range(1, len(dg)) if outdegrees[i] == 0)
	# invariant, if in queue, all children processed
	while queue:
		node = queue.popleft()
		grundy[node] = mex([grundy[child] for child in dg[node]])
		for p in rdg[node]:
			outdegrees[p] -= 1
			if outdegrees[p] == 0:
				queue.append(p)
	count = Counter(grundy[1:])
	return count


def solve():
	n, m = map(int, input().split())
	dg = [[] for _ in range(n + 1)]
	outdegrees = [0 for _ in range(n + 1)]
	for _ in range(m):
		u, v = map(int, input().split())
		dg[u].append(v)
		outdegrees[u] += 1
	counts = compute_grundy_numbers(dg, outdegrees)
	mcount = max(counts) + 2
	A = [[-counts[i ^ j] / (n + 1) for j in range(mcount)] for i in range(mcount)]
	b = [1 / (n + 1) for i in range(mcount)]
	b[0] = 0
	for i in range(mcount):
		A[i][i] += 1
	A = np.array(A)
	#print(A[:5])
	b = np.array(b)
	sol = np.linalg.solve(A, b)
	#print(sol)
	MOD = 998244353
	# numpy gives us a fraction, convert to two primes
	frac = Fraction(sol[0]).limit_denominator(MOD)
	P, Q = frac.numerator, frac.denominator
	#print(P, Q, sol[0])
	# use fermats lil therum
	ans = (P * pow(Q, MOD - 2, MOD)) % MOD
	print(ans)


solve()
