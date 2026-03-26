def first_out_of_order(s):
	for i in range(len(s)-1):
		if s[i] > s[i+1]: return i
	return None
class Solution:
	def minOperations(self, s: str) -> int: # TODO: annoying impl problem
		n = len(s)
		s = list(s)
		if any(s[i] > s[i+1] for i in range(n-1)) and n == 2: return -1
		res = 0
		while any(s[i] > s[i+1] for i in range(n-1)):
			idx = first_out_of_order(s)
			end = min(idx+n-1, n)
			s[idx:end] = sorted(s[idx:end])
			res+=1
			print(s)
		return res
