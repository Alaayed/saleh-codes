# link: https://codeforces.com/contest/2209/problem/C

def solve():
    n = int(input())
    init_idx = 1
    diff_idx = -1
    for i in range(n+1):
        print(f'? {init_idx} {init_idx+i}')
        response = int(input())
        if response == 1: # is zero 
            while diff_idx == -1:
                i+=1
                print(f'? {init_idx} {init_idx+i}')
                response = int(input())
                if response == 0: diff_idx = i+init_idx
            print(f'! {diff_idx}')
solve()