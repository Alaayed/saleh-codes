from typing import *
def isAchievable(target: int, nums: Set[int] ):
	for i in nums:
		if target ^ i in nums: return True
	return False
class Solution:
	def findMaximumXOR(self, nums: List[int]) -> int:
		x = 0
		nums = set(nums)
		for i in range(30, -1, -1):
			cur_bit = 1 << i
			if (isAchievable(cur_bit | x, nums)): # Big O (N) check
				x |= cur_bit # add bit

		return x

nums = [[3,10,5,25,2,8],
[14,70,53,83,49,91,36,80,92,51,66,70]]
for n in nums:
	print(Solution().findMaximumXOR(n))
