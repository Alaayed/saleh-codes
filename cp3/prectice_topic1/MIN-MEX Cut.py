def stripOfOnes(s: str):
    startIndex = 0
    endIndex = 0
    for i,c in enumerate(s):
        if c != '1':
            startIndex = i
            break
    for i,c in enumerate(reversed(s)):
        if c != '1':
            endIndex = len(s) - i
            break
    return s[startIndex : endIndex]

def solve():
    t = int(input())
    res = []
    for _ in range(t):
        bitstring = input()
        bitstring = stripOfOnes(bitstring)
        if '1' in bitstring and '0' in bitstring:
            res.append(2)
        elif '0' in bitstring:
            res.append(1)
        else:
            res.append(0)
    list(map(print,res))
solve()