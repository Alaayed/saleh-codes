from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        s = defaultdict(int)
        s[nums[0]] +=1
        cur = nums[0]
        for i in nums:
            if i != cur:
                cur = i
                s[cur] +=1
        return sum ([1 if v == 1 else 0 for v in s.values()])
        
