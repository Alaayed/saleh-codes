# link: https://codeforces.com/group/xSQ0pfWy2O/contest/674999/problem/B
STRAIGHT = 1
BACKWARD = -1
def orientation(turn):
	if turn ==0: return 1
	if turn % 2 != 0:return 1
	else: return -1
def solve_test_case():
	n = int(input())
	a = input()
	b = input()
	#print(a,b)
	ds = sum([1 if a[i] != b[i] else 0 for i in range(n)])
	if ds == 0: return 0
	db= sum([1 if a[i] != b[-1-i] else 0 for i in range(n)])
	if db == 0 and ds != 1: return 2
	# print(diffs_straight,diffs_backwards)
	# straight_completion = diffs_straight*2 +(-1 if diffs_straight % 2 == 1 else 0)
	# backward_completion = diffs_backwards*2 + (-1 if diffs_backwards % 2 != 1 else 0)
	# if diffs_backwards == 0: backward_completion = 2
	sc = ds + ((ds-1) if orientation(ds) == STRAIGHT else ds)
	bc = db + ((db-1) if orientation(db) == BACKWARD else db)
	return min(sc, bc)
def solve():
	test_cases = int(input())
	results= []
	for _ in range(test_cases):
		results.append(solve_test_case())

	list(map(print,results))
solve()