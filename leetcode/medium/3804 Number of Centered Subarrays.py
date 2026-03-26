# link:https://leetcode.com/problems/number-of-centered-subarrays/description/
from typing import *
def is_centered(i,j,nums):
	return sum(nums[i:j+1]) in nums[i:j+1]
class Solution:
	def centeredSubarrays(self, nums: List[int]) -> int:
		n=len(nums)
		res = 0
		for i in range(n):
			for j in range(i+1,n):
				res+= is_centered(i,j,nums)
		return res