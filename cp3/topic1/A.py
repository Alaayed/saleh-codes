from math import gcd
def prime_factorize(num):
    factors = set()
    divisor = 2
    if num % 2 == 0: # handle two case specially
        while num % 2 == 0:
            num //= 2
        factors.add(2)
        divisor += 1
    while num != 1:
        if num % divisor == 0:
            factors.add(divisor)
            num /= divisor
        else:
            divisor += 2 # skip half the numbers
    return list(factors)
def create_masks(nums: list[int], factors: list[int]):
    masks = []
    for num in nums:
        mask = 0
        for i,factor in enumerate(factors):
            if num % factor == 0:
                mask |= 1 << i
        masks.append(mask)
# dp[cur][mask] best cost given the first cur elements to cover the mask


def solve():
    n = int(input())
    nums = list(map(int , input().split()))
    costs = list(map(int, input().split()))
    for i,num in enumerate(nums):
        factors = prime_factorize(num)
        masks = create_masks(factors, nums)
        dp_table = [[-1 for _ in range( 1<<len(factors))] for _ in range(n)]
        optMask = 1<<len(factors) -1
        optCost = dp(i, 0, 0)
        def dp(cur, mask, cost) -> int:
            if cur == n:
                return cost if mask == optMask else float('inf')
            # Two decisions, take the current option or not
            dp_table[cur][mask] = min( dp(cur+1, mask, cost) , dp (cur, mask | masks[cur], cost + costs[cur]) )
solve()