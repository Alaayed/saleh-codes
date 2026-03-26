from collections import defaultdict
from typing import *
def digit_frequency(n):
	freq = defaultdict(int)
	for digit in str(n):
		freq[int(digit)] += 1
	return freq
class Solution:
	def isDigitorialPermutation(self, n: int) -> bool:
		temp =1
		fact = [1] + [temp := temp * (i) for i in range(1, 10)]
		# Get factorial of each digit
		res =0
		init_n = n
		while n != 0:
			first_digit = n % 10
			n = n // 10
			res += fact[first_digit]
		# find if digits can be rearranged
		a = digit_frequency(res)
		b = digit_frequency(init_n)
		return a == b

sol = Solution()
print(sol.isDigitorialPermutation(415))