from collections import defaultdict
from typing import *

memo = defaultdict(str)


def construct_nth(n):
	if n == 1: return '0'
	if memo[n]: return memo[n]
	left = construct_nth(n-1)
	right = construct_nth(n-1)[::-1]
	right_inv = ''.join('0' if bit == '1' else '1' for bit in right)
	memo[n] = left + '1' + right_inv
	return memo[n]

class Solution:
	def findKthBit(self, n: int, k: int) -> str:
		nth_str = construct_nth(n)
		return nth_str[k-1]

