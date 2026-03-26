# link: https://leetcode.com/problems/combination-sum-iii/

from typing import *
from itertools import combinations
class Solution:
	def combinationSum3(self, k: int, n: int) -> List[List[int]]:
		res = []
		for comb in combinations(range(1, 10), k):
			if sum(comb) == n:
				res.append(list(comb))
		return res