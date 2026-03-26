# link: https://codeforces.com/group/xSQ0pfWy2O/contest/668150/problem/C
# Okay, when moving from the jth to jth+1 column,
# We don't have to recompute the max for all the n sliding arrays
# if we have to recompute the value for a sliding array of length k,
# we have to recompute the value for all sliding arrays of length >= k
# make all arrays sparse tables for O(1) max range queries
# Keep a prefix sum for all values that don't need to be recomputed (all values reachable)
from collections import Counter, deque
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
		if not self.h: return 0
		return -self.h[0]

from typing import*
def generate_events(a, w):
	"""
	Given a, generate all 2*l add delete events
	"""
	add = []
	rem = []
	l = len(a)
	for i in range(l):
		add.append([i,a[i]])
		# the last valid start, then move to ith position
		rem.append([w-l + i, a[i]])
	if l != w:
		add.append( [0, 0] )
		rem.append( [w-l-1, 0])
		add.append( [l, 0])
		rem.append( [w-1,0])
	add.sort()
	rem.sort()
	return deque(add), deque(rem)
def handle_events(diff: List[int],add: Deque[int], rem: Deque[int]):
	multiset = MaxSet()
	prev_idx = 0
	def range_add(l , r, val): # Helper
		if l <= r:
			diff[l]+= val
			diff[r+1]-= val
	while add or rem:
		# [prev_idx ... idx]
		# values need to be assigned
		# from prev_idx to idx-1, nothing happened
		# range update
		idx = min(add[0][0] if add else len(diff), rem[0][0])
		range_add(prev_idx, idx-1, multiset.get_max())
		# Now, time to update the multiset
		while add and add[0][0] == idx:
			_, value = add.popleft()
			multiset.add(value)
		# Now, update location idx
		range_add(idx, idx, multiset.get_max())
		# Now, values that are not valid
		while rem and rem[0][0] == idx:
			_, value = rem.popleft()
			multiset.rem(value)
		# update prev idx
		prev_idx = idx+1


def solve():
	n,w = map(int,input().split())
	diff = [0] * (w+1)
	for _ in range(n):
		num = list(map(int,input().split()))[1:]
		add: Deque[int]
		rem: Deque[int]
		add, rem = generate_events(num, w)
		handle_events(diff, add, rem)
	prefix=0
	print(*[prefix:= prefix + j for j in diff[:len(diff)-1]])

solve()