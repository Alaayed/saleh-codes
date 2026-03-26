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