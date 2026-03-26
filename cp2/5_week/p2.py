class Fenwick():
		def __init__(self, size):
			self.tree = [0 for _ in range(size+1)]
		def add(self, value, index):
			while index < len(self.tree):
				self.tree[index] += value
				index += index & (-index)
		def query(self, index):
			ret = 0
			while index > 0:
				ret += self.tree[index]
				index -= index & (-index)
			return ret
		def tp(self):
				print(self.tree)
		def rangeq (self , l , r):
			return self.query(r)-self.query(l-1)
def mega_inversions():
	# Use two BITs 
	# First one counts the number of inversions
	# Second stores the inversions counted
	UPPER = int(1e5)
	t1 = Fenwick(UPPER)
	t2 = Fenwick(UPPER)
	_ = input()
	nums = list(map(int , input().split()))
	res = 0
	for n in nums:
		# t1
		t1.add(value =1 , index = n)
		inv = t1.rangeq( l = n+1 , r = UPPER)
		# t2
		t2.add(value = inv, index = n)
		res+= t2.rangeq(l = n+1, r = UPPER)
	print(res)
mega_inversions()
