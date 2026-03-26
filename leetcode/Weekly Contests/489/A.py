from typing import *
class Solution:
	def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
		elements = set()
		for b in bulbs:
			if b in elements: elements.remove(b)
			else: elements.add(b)
		return sorted(list(elements))