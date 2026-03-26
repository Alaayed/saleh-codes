from typing import *
from bisect import bisect_left
class Solution:
	def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
		idx, val = -1, float('inf')
		for i,c in enumerate(capacity):
			if itemSize <= c and c < val:
				idx = i
				val = c
		return idx