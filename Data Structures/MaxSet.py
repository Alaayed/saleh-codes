from collections import Counter
import heapq
class MaxSet:
	def __init__(self):
		self.h = []
		self.cnt = Counter()
	def add(self, x):
		self.cnt[x] += 1
		heapq.heappush(self.h,-x)
	def rem(self, x):
		self.cnt[x] -= 1
	def get_max(self):
		while self.h and self.cnt[-self.h[0]] == 0:
			heapq.heappop(self.h)
		if not self.h: print("ISSUE")
		return -self.h[0]