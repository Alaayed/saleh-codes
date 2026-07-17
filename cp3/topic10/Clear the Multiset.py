# link: https://codeforces.com/group/xSQ0pfWy2O/contest/683109/problem/A
from math import ceil, floor
def remove_mid_range(a):
	na = a.copy()
	n = len(a)
	if n % 2 == 0: il,ir = n//2-1, n//2
	else: il,ir = n//2, n//2
	l,r = il,ir
	lmin = a[l]
	rmin = a[r]
	while l != 0:
		lmin = min(na[l] , lmin)
		na[l] -= lmin
		l-=1
	while r != n:
		rmin = min(na[r] , rmin)
		na[r] -= rmin
		r+=1
	return na, max(a[ir], a[il])
def rec(a):
	n= len(a)
	# base case
	if n == 1: return 1
	# case 1: removing mid range is optimal
	na, cost = remove_mid_range(a)
	print(na)
	lcost, rcost = rec(na[:n//2]), rec(na[n//2:])
	case1_cost = cost+lcost+rcost
	# case 2: let them handle it
	lcost, rcost = rec(a[:n//2]), rec(a[n//2:])
	return min(case1_cost, lcost+rcost)
def solve():
	n = int(input())
	a = list(map(int, input().split()))
	print(rec(a))
solve()