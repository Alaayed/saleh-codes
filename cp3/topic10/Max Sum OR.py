def solve_testcase():
	_,r = map(int,input().split())
	res = []
	s  =0
	j = 0
	for i in range(r,-1, -1):
		s += i | j
		res.append(i)
		j+=1
	print(s)
	print(*res)
def solve() :
	t = int(input())
	while t:
		solve_testcase()
		t-=1

solve()