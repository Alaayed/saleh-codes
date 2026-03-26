from typing import *
class Solution:
	def trimTrailingVowels(self, s: str) -> str:
		vowels = ['a', 'e', 'i', 'o', 'u']
		while s and s[-1] in vowels: s = s[:-1]
		return s
