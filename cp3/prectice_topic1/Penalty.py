# link: http://codeforces.com/problemset/problem/1553/C
# Just a simple greedy? Assume team 1 does amazing and see min then do the same for team 2
def minWin(s, team):
    allyScore = 0
    enemyScoringPotential = 5
    enemyScore = 0
    for i,c in enumerate(s):
        if c == '?' and i % 2 == team:
            allyScore +=1 
        elif c == '?':
            enemyScoringPotential -= 1
        elif c == '1':
            if i % 2 == team:
                allyScore += 1
            else:
                enemyScore +=1
                enemyScoringPotential -= 1
        elif c == '0':
            if i % 2 == team:
                allyScore += 0
            else:
                enemyScoringPotential -= 1
        if enemyScore + enemyScoringPotential < allyScore:
            return i+1
    return 10
def solve():
    t = int(input())
    allBitStrings = [input() for _ in range(t)]
    allSolutions  = [min(minWin(s, 0),minWin(s,1)) for s in allBitStrings]
    list(map(print,allSolutions))
solve()