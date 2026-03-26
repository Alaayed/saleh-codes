from typing import *
class Solution:
	def chalkReplacer(self, chalk: List[int], k: int) -> int:
		total = sum(chalk)
		remaining_k = k % total
		for i,c in enumerate(chalk):
			remaining_k -= c
			if remaining_k < 0:
				return i
		return len(chalk)-1