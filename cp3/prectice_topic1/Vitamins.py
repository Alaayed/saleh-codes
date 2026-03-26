# link:https://codeforces.com/problemset/problem/1042/B
# try all permuations should work since 1000 choose 3 < 1e9
def convertToMask(s):
    val = 0
    if 'A' in s:
        val += 1
    if 'B' in s:
        val += 2
    if 'C' in s:
        val += 4
    return val
def solve():
    n = int(input())
    juices = [ [int(i), convertToMask(j)] for i,j in [input().split() for _ in range(n)]]
    minCost = float('inf')
    for i in range(n):
        im = juices[i][1]
        if (im) == 7:
            minCost= min(juices[i][0], minCost)
        for j in range(i+1, n):
            jm = juices[j][1]
            if (jm | im) == 7:
                minCost= min(juices[i][0] +juices[j][0], minCost)
            for k in range(j+1, n): 
                km = juices[k][1]
                if (im | jm | km) == 7:
                    minCost= min(juices[i][0] +juices[j][0] + juices[k][0], minCost)
    print(minCost if minCost != float('inf') else -1)
solve()