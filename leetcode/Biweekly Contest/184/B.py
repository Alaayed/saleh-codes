from math import ceil


def merge_intervals(intervals):
	unified_intervals = []
	intervals.sort()
	for s, e in intervals:
		if unified_intervals and unified_intervals[-1][1] >= s:
			unified_intervals[-1][1] = max(unified_intervals[-1][1], e)
		else:
			unified_intervals.append([s, e])
	return unified_intervals
def sum_merged_intervals(intervals):
	sum = 0
	for start, end in intervals:
		sum += end - start +1
	return sum
class Solution:
	def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
		unified_intervals = merge_intervals(intervals)
		total_time = sum_merged_intervals(unified_intervals)
		bulbs_per_time = ceil(brightness / 3)
		return total_time * bulbs_per_time



n = 4
b = 2
i = [[1,3],[2,4]]
print(Solution().minEnergy(n, b, i))