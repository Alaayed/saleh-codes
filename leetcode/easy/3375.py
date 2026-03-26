from typing import *
class Solution:
	def minOperations(self, nums: List[int], k: int) -> int:
		min_element = min(nums)
		if min_element >= k: return len(set(nums)) - (min_element == k)
		return-1
