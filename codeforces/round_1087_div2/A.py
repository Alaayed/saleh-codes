# https://codeforces.com/contest/2209/problem/A
import bisect
def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n,c,k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        idx = bisect.bisect_right(a, c)
        while idx != 0: 
            diff = abs(c-a[idx-1])
            c += min(k+a[idx-1], c)
            a.pop(idx-1)
            k -= min(diff,k)
            idx = bisect.bisect_right(a, c)
        res.append(c)
    list(map(print, res))
solve()