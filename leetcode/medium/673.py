# node (l,r,lenght)


class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        # push dp 
        dp = [1 for i in range(n)]
        count = [1 for i in range(n)]
        # dp[i], longest strictly increasing sequence ending at i
        for i in range(n):
            end = nums[i]
            # push dp[i] up 
            j = i+1
            while j != n:
                next = nums[j]
                if end < next: 
                    if dp[i]+1 == dp[j]: # count[i], since the number of ways to make dp[j] increased by count[i]
                        count[j] += count[i]
                    elif dp[i]+1 > dp[j]: # number of ways to make j is now the number of ways to make i
                        dp[j] = dp[i]+1
                        count[j] = count[i]
                j+=1
        maxss = max(dp)
        return sum([count[i] if dp[i] == maxss else 0 for i in range(n) ])
