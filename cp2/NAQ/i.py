def solve():
	n = int(input())
	l1 = list(map(int , input().split()))
	l2 = list(map(int , input().split()))
	l2.sort()
	running= 0
	mav = -1
	for i in range(n):
		ps = l1[i]
		running += l2[i]
		mav = max(mav,  (ps+running) / (i+1))
	print(mav)
solve()
