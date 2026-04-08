# link: https://codeforces.com/problemset/problem/1097/B

# simple brute force

def solve():
    n = int(input())
    rotations = [int(input()) for i in range(n)]
    # 1 << 3 -> 1000
    # iterate till 0111 makes sense
    for S in range(1 << n):
        stateSum = 0
        for i in range(n):
            stateSum += rotations[i] if (1 << i) & S else -rotations[i]
        if stateSum % 360 == 0:
            print('YES')
            return
    print('NO')
solve()