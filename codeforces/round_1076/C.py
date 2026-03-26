def maximize_sum(a,b):
	res = []
	for i in range(-1, -len(a)-1,-1):
		res.append(max(a[i], b[i], res[-1] if res else 0))
	return list(reversed(res))
class Fenwick:
	def __init__(self, n):
		self.tree = [0 for _ in range(n+1)]
		self.n = n
	def rsq_query(self, l , r):
		return self.query(r)-self.query(l-1)
	def query(self, i):
		res = 0
		while i > 0:
			res += self.tree[i]
			i -= i & -i
		return res
	def update(self, i, value):
		while i <= self.n:
			self.tree[i] += value
			i += i & -i
	def array_update(self, a):
		for i in range(self.n):
			self.update(i+1, a[i])
def solve():
	for _ in range(int(input())):
		n,q = map(int,input().split())
		a = list(map(int,input().split()))
		b = list(map(int,input().split()))
		# get the maximization
		greedy = maximize_sum(a,b)
		# Create and update the fenwick tree
		fenwick = Fenwick(n)
		fenwick.array_update(greedy)
		res = []
		for _ in range(q):
			l,r = map(int,input().split())
			res.append(fenwick.rsq_query(l,r))
		print(*res)
solve()