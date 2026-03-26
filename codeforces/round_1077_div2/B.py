# https://codeforces.com/contest/2188/problem/B


# For each subsequence of straight zeros,
# get the number of zeros with no adj 1
# Divide number of zeros by 3 then ciel
# Gives you the number of additional students to add
# 10001

from math import ceil
def conseq_zeros(s:str):
	last_one = s.find('1')
	if last_one == -1:
		return [len(s)]
	diff = []
	for i,c in enumerate(s):
		# 10001, only care about zeros with no neighbors
		if c == '1':
			if (i-last_one-3)>0:
				diff.append(i-last_one-3)
			last_one = i
	first_one = s.find('1')
	if first_one > 1:
		diff.append(first_one-1)

	last_one = s[::-1].find('1')
	if last_one > 1:
		diff.append(last_one-1)
	return diff

def solve():
	for _ in range(int(input())):
		n = int(input())
		bitstring = input()
		zeros = conseq_zeros(bitstring)
		min_ones_needed = sum( ceil(i/ 3) for i in zeros) + bitstring.count('1')
		print(min_ones_needed)
solve()