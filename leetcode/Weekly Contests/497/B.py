from math import sin 
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        largest = max(sides)
        remaining = sides.remove(largest)
        remaining = list(map(lambda x: x**2, remaining))
        # is triangle
        if largest**2 != sum(remaining): return []
        # SOH CAH TOA 
        