# link : https://codeforces.com/group/xSQ0pfWy2O/contest/665471/problem/C


def solve():
    n,l,r,x = map(int, input().split())
    difficulty = list(map(int, input().split()))
    difficulty.sort()
    possible_subsets = 0
    for S in range(1 << n):
        if S.bit_count() >= 2:
            minElement = float('inf')
            maxElement = -1
            sumDifficulty = 0
            for i,c in enumerate(difficulty):
                if ((1 << i) | S) == S: # if the ith bit is set
                    minElement = min(minElement , c)
                    maxElement = max(maxElement, c)
                    sumDifficulty += c
            if l <= sumDifficulty <= r and abs(minElement - maxElement) >= x:
                possible_subsets += 1
    print(possible_subsets)
solve()