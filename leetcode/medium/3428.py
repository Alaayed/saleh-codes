# link: https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/description/
from typing import *
mod = 10**9 + 7
def build_fact(n):
    fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i % mod

    invfact = [0] * (n+1)
    invfact[n] = pow(fact[n], mod - 2, mod)

    for i in range(n-1, -1, -1):
        invfact[i] = invfact[i+1] * (i+1) % mod

    return fact, invfact
fact, invfact = build_fact(10**5 + 5)
def choose (n,k):
    if k > n: return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % mod
def count_subsequences(n,k):
    return sum(choose(n,i) for i in range(1,k+1))
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i,val in enumerate(nums):
            larger_elements = n-i-1
            smaller_elements = i
            # lone case
            result = (result + val*2 ) % mod
            # min case
            result = (result + val*count_subsequences(larger_elements,k-1)) % mod
            # max case
            result = (result + val*count_subsequences(smaller_elements,k-1))% mod
        return result

sol = Solution()
print(sol.minMaxSums(nums = [1,1,1], k = 2))