
class JaggedSparseTable:
	def __init__(self, a):
		self.st = [a[:]]
		n = len(a)
		k = 1
		while (1 << k) <= n:
			prev = self.st[-1]
			step = 1 << (k - 1)
			cur = [
				max(prev[i], prev[i + step])
				for i in range(n - (1 << k) + 1)
			]
			self.st.append(cur)
			k += 1

	def query(self, l, r, idempotent=True):
		if idempotent:
			length = r - l + 1
			k = length.bit_length() - 1
			return max(self.st[k][l], self.st[k][r - (1 << k) + 1])
import numpy as np
import random
class SparseTester:
	def __init__(self):
		pass
	def mid_test(self, tests):
		array = np.random.randint(0,100,1_000).tolist()
		table = JaggedSparseTable(array)
		for _ in range (tests):
			l,r = sorted([random.randint(0,999) for _ in range(2)])
			if max(array[l:r+1]) != table.query(l,r,idempotent=True):
				print('ISSUE DETECTED')
		print('NO ISSUES')
tester = SparseTester()
tester.mid_test(1000)