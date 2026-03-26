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
fact, invfact = build_fact(2*10**5 + 5)
def choose (n,k):
    return (fact[n] * invfact[k] * invfact[n-k]) % mod
def solve():
    for _ in range(int(input())):
        n,m = map(int, input().split())
        ranges = [list(map(int, input().split())) for i in range(m)]
        a= [0 for _ in range(n)]
        for i,j,val in ranges:
            a[i-1] |= val
        bits = [0 for _ in range(30)]
        # Calculate how many times each bit is a one
        for i in range(30):
            for e in a:
                bits[i] += 1 if (e & (1<<i)) != 0 else 0
        total_contribution = 0
        for i in range(30):
            onebits = bits[i]
            zerobits = n-onebits
            if onebits > 0: # 2^n-1 odd ways to pick one bits
                bit_contribution= ((1 << (onebits-1)) * (1 << zerobits)) % mod
            else:
                bit_contribution = 0
            # ith bit contribution 2^i value
            bit_contribution *= (1 << i)
            bit_contribution %= mod
            total_contribution += bit_contribution
            total_contribution %= mod
        print(total_contribution)
solve()