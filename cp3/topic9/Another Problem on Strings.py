# link : https://codeforces.com/group/xSQ0pfWy2O/contest/681486/problem/A
def solve_special_case(s):
	zc = 0
	res = 0
	for c in s:
		if c == '0': zc+=1
		else:
			res += (zc *(zc+1))//2
			zc = 0
	res += (zc*(zc+1))//2
	print(res)
def count_zeros(s: str):
	ones_count = s.count('1')
	zeros_prior = [0] * ones_count
	zeros_post = [0] * ones_count
	if ones_count == 0:
		return zeros_prior, zeros_post
	zc = 0
	cur_one = 0
	for i,c in enumerate(s):
		if c == '0':
			zc+=1
		else:
			if cur_one != 0: zeros_post[cur_one-1] = zc
			zeros_prior[cur_one] = zc
			zc = 0
			cur_one += 1
	zeros_post[cur_one-1] = zc
	return zeros_prior, zeros_post
def solve():
	k = int(input())
	s = input()
	if k == 0:
		solve_special_case(s)
		return
	zeros_prior, zeros_post = count_zeros(s)
	cur_one = 0
	res = 0

	while cur_one + (k-1) < len(zeros_prior) and zeros_prior:
		res += (zeros_prior[cur_one]+1) * (zeros_post[cur_one+k-1]+1)
		cur_one +=1
	print(res)
# print(count_zeros('0001001000'))
# print(count_zeros('001110'))

solve()