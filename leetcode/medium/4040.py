class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        # let dp[i,j] be the minimum number of operations required for i to become j
        dp = [ [0 for _ in range(sum)] for _ in range(len(nums))]
        for i,v in enumerate(nums):
            t = v
            # multiplication
            co = 0
            while t <= sum:
                dp[i][t] = co
                t <<= 1
                co +=1
            # division
            t = v
            co = 0
            while t > 0: 
                dp[i][t] = co
                t >>= 1
                co += 1

        # For each on
        return 0 
