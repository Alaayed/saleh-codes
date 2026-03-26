import math
VICTORY_MESSAGE = "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
LOSS_MESSAGE    = "RECOUNT!"
OTHER_MESSAGE   = "PATIENCE, EVERYONE!"
suffix_sum_pascal = []
def precompute_suffix_sum():
	for i in range(51):
		suffix_sum_pascal.append(compute_row_suffix_sum(i))
def compute_row_suffix_sum(i):
	elements = i+1
	row_sum = pow(2, i)
	res = [row_sum]
	for j in range(1, elements):
		res.append(res [j-1] - math.comb(i , j-1))
	return res

def election(n, v1, v2, w):
	min_voters_needed = max(0,n // 2 - v1 + 1)
	undecided = n - v1 - v2
	ways_to_win = 0
	if min_voters_needed <= undecided:
		ways_to_win = suffix_sum_pascal[undecided][min_voters_needed]
	victory_percentage= (ways_to_win/ (2 ** (undecided))) * 100
	if victory_percentage > w:
		print(VICTORY_MESSAGE)
	elif victory_percentage == 0:
		print(LOSS_MESSAGE)
	else:
		print(OTHER_MESSAGE)

def read_in():
	precompute_suffix_sum()
	test_cases = int(input())
	for _ in range(test_cases):
		# Check if W can be a float
		line = input().split()
		(n, v1, v2, w) =map(int, line) 
		election(n=n, w=w, v1=v1, v2=v2)
read_in()
