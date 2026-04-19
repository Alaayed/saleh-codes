# link: https://codeforces.com/contest/2209/problem/B
import bisect


def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        tres = []
        for i in range(n):
            indices = a[i+1:]
            # print(f"Indices: {indices}")
            indices.sort()
            idx = bisect.bisect_left(indices, a[i])
            below = idx 
            above = len(indices) - idx - abs(idx - bisect.bisect_right(indices, a[i]))
            # print(f"Below: {below}, Above: {above}")
            tres.append(max(below, above))
        res.append(tres)
    for r in res:
        print(*r)
solve()