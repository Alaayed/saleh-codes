from typing import *
def construct_intervals(s):
	intervals = []
	prev = False
	start=0
	end = 0
	for i in range(len(s)):
		if s[i] == '1':
			if not prev: start = i
			prev = True
		else:
			if prev == True:
				end = i-1
				intervals.append([start,end])
			prev = False

	if prev == True:
		intervals.append([start,len(s)-1])
	print(intervals)
	return intervals


class Solution:
	def maxTotal(self, nums: List[int], s: str) -> int:
		intervals = construct_intervals(s)
		msum = 0
		for s,e in intervals:
			s1 = sum(nums[s:e+1])
			s2 = sum(nums[s-1:e]) if s != 0 else 0
			msum += max(s1,s2)
		return msum


		return 0


# construct_intervals('11101110111')
# construct_intervals('11101111111')
# construct_intervals('00000000000')