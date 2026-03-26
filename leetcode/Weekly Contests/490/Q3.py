from typing import *
def count_ones(s):
	return sum( [i == '1' for i in s] )
class Solution:
	def maximumXor(self, s: str, t: str) -> str:
		soc,toc,n = count_ones(s), count_ones(t), len(s)
		rem = toc+soc - n
		res = ['1'] * n
		nt  = ['0'] * n
		# Pick the top rem LSBs of s
		for i in range(n):
			if s[-1-i] and rem > 0:
				nt[-1-i] = '1'
				rem -= 1
			if rem <= 0:
				break
		nt = ''.join(nt)
		print(nt)
		for i,(a,b) in enumerate(zip(s,nt)):
			if a == b == '1':
				res[i] = '0'
		return ''.join(res)






sol = Solution()
print(sol.maximumXor('1','1' ))