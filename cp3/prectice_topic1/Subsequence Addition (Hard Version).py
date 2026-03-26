# link: https://codeforces.com/problemset/problem/1807/G2
# My main issue is figuring out if
# Given an array a and target k you can find if a subset of a sums to k
# Initially I thought that a greedy 'always pick the largest' works
# but I can think of a counter example
# a: [5,5,9], k = 10
# Regret greedy? that fails to this case
# a: [1,5,9], k = 10

def is_possible(c):
    if c[0] != 1:
        return False
    current_sum = 1
    for num in c[1:]:
        #print(f'current_sum, num, condition: {current_sum}, {num}, {current_sum < num}')
        if current_sum < num:
            return False
        current_sum += num
    return True

def solve():
    t = int(input())
    res = [ ]
    for _ in range(t):
        n = int(input())
        c = sorted(list(map(int , input().split())))
        res.append( "YES" if is_possible(c) else "NO")
    list(map(print, res))
solve()