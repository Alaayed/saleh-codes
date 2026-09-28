# link : https://codeforces.com/problemset/problem/2146/D1
def solve():
    _,r = map(int, input().split())
    # i.e. if r:b = 1111
    output = [0 for _ in range(r+1)]
    high = r
    while high > -1:
        mask = (1 << (high.bit_length())) - 1
        low = mask - high
        #print(f'low,high,mask {low},{high},{mask}')
        for i in range(low, high+1): output[i] = mask - i
        high = low-1
    print(sum(i ^ output[i] for i in range(r+1)))
    print(" ".join(list(map(str, output))))
for _ in range(int(input())): solve()
