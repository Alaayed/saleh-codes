from typing import *
def swap(a):
	if a: return False
	else: return True
class Solution:
	def scoreDifference(self, nums: List[int]) -> int:
		n = len(nums)
		is_firsts_turn = True
		first_score = 0
		second_score = 0
		for i in range(n):
			# apply rule 1
			if nums[i] % 2 == 1: is_firsts_turn = not is_firsts_turn
			# apply rule 2
			if i % 6 == 5: is_firsts_turn = not is_firsts_turn
			if is_firsts_turn: first_score += nums[i]
			else: second_score += nums[i]
		return first_score - second_score




