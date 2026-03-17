from typing import *
class Solution:
	def smallestBalancedIndex(self, nums: list[int]) -> int:
		total = 0
		prefix_sum = [total := total + i for i in nums] + [0]
		suffix_prod= 1
		idx=len(nums)-1
		bidx= -1
		while idx>0:
			if prefix_sum[idx-1] == suffix_prod: bidx = idx
			if prefix_sum[idx-1] <  suffix_prod: return bidx
			suffix_prod*=nums[idx]
			idx-=1
		return bidx
	# DONE: Implement overflow checks, python just blows up memory since constraints specify nums[i] <= 10^9