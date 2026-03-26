# problem link https://codeforces.com/problemset/problem/1566/C

# First solution. If expanding a bi table increases the solution, you should
# Note: Expanind a bi table containing 1 into [1,0] is equiv to just ending the bi table
# Note^2: Expanding a bi table containing 0 into [1,0] is SUBOPTIMAL! You should start and end a new bitable 
# Not expanding is never suboptimal if you have a value of 2
def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        firstBS = input()
        secondBS= input()
        totalSum = 0
        i= 0
        prev = -1
        while (i != n):
            hasOne = firstBS[i] == '1' or secondBS[i] == '1'
            hasZero= firstBS[i] == '0' or secondBS[i] == '0'
            # has Score of 2
            if (hasOne and hasZero):
                #Skip this
                totalSum += 2
                i+=1 
                prev = 2
            elif hasZero: # is a zero
                totalSum += 1
                i += 1
                if prev == 1: # Merge the previous one
                    totalSum +=1
                    prev = 2
                else: # Note that there was a previous 0
                    prev = 0
            elif hasOne:
                i+=1
                # Two cases, had a zero before or didnt.
                if prev == 0: # If zero, merge
                    totalSum += 1
                    prev = 2
                else: # If not, just note there is one for merging
                    prev = 1
        res.append(totalSum)
    list(map(print, res))
solve()
