from collections import defaultdict
from typing import *
class Solution:
	def firstUniqueFreq(self, nums: List[int]) -> int:
		# Get first apperance
		first_appear = defaultdict(int)
		# Count freq
		freqs = defaultdict(int)
		for i,e in enumerate(nums):
			if e not in first_appear:
				first_appear[e] = i
			freqs[e] += 1
		# eliminate dups
		freq_count = defaultdict(int)
		for k,v in freqs.items():
			freq_count[v] += 1
		filtered_keys = [k for k,v in freqs.items() if freq_count[v] == 1]
		rem = [[v,k] for k,v in first_appear.items() if k in filtered_keys]
		return min(rem)[1] if rem else -1
