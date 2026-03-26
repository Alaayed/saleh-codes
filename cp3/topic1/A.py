from math import sqrt, floor



def prime_factorize(num):
    factors = set()
    if num % 2 == 0:  # handle two case specially
        while num % 2 == 0:
            num //= 2
        factors.add(2)
    i = 3
    while i * i <= num:
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num //= i
        i += 2
    if num > 1:
        factors.add(num)
    return list(factors)


def create_masks(nums: list[int], factors: list[int]):
    masks = []
    for num in nums:
        mask = 0
        for i, factor in enumerate(factors):
            if num % factor != 0:
                mask |= 1 << i
        masks.append(mask)
    return masks


# dp[cur][mask] best cost given the first cur elements to cover the mask


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    optCost = float('inf')
    for i, num in enumerate(nums):
        factors = prime_factorize(num)
        masks = create_masks(nums, factors)
        dp_table = [[-1 for _ in range(1 << len(factors))] for _ in range(n)]
        optMask = (1 << len(factors)) - 1

        def dp(cur, mask) -> int:
            if cur == (n - 1):
                if dp_table[cur][mask] != -1:  #
                    return dp_table[cur][mask]
                if mask == optMask:  # Mask already complete, no additional cost incurred
                    dp_table[cur][mask] = 0
                elif (masks[cur] | mask) == optMask:  # Not complete, but nth element completes it
                    dp_table[cur][mask] = costs[cur]
                else:  # Cannot be completed, return inf
                    dp_table[cur][mask] = float('inf')
                return dp_table[cur][mask]
            if dp_table[cur][mask] != -1:
                return dp_table[cur][mask]
            # Two decisions, take the current option or not
            dp_table[cur][mask] = min(
                dp(cur + 1, mask),  # Don't, keep the mask the same
                dp(cur + 1, mask | masks[cur]) + costs[cur])  # do, change the mask
            return dp_table[cur][mask]

        optCost = min(optCost, dp(i, 0) + costs[i])
# Given a mask, what is the minimum cost to complete the mask using cur, cur+1,...n-1,n?

    print(optCost if optCost != float('inf') else -1)
    return None

solve()
