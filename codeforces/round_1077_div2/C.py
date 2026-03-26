# link: https://codeforces.com/contest/2188/problem/C

# I think there exists a greedy assumption at the core of this
# Assumption: It's always optimal to swap an element into position
# meaning, if we have 66,0,100
# it's there exists no other optimal path for the problem,
# than swaping 0 with 100
# 4,1,100
# 100,1,4
# 1,100,4
# omg,  you just use the largest element as
# an intermezzo
# find the largest element that is not in order then the answer is
# doesnt work lmao
# 1 1 4 5 1 4
# for any series of swap i,j
# There are three choices only.
# 1 and 2: use either the largest or smallest element as an
# intermezzo, or  just outright swap
def all_out_of_order_pairs(a: list[int]):
	a_sorted = sorted(zip(a, [i for i in range(len(a))]))
	#print(a_sorted)
	return [[i,j] for i,(_,j) in enumerate(a_sorted)  if i != j and i < j]
def solve():
	for _ in range(int(input())):
		n = int(input())
		nums = list(map(int, input().split()))
		if all( nums[i] <= nums[i+1] for i in range(len(nums) -1)):
			print(-1)
			continue
		#print(* all_out_of_order_pairs(nums))
		pairs = all_out_of_order_pairs(nums)
		largest = max(nums)
		smallest= min(nums)
		best_swap_for_pairs = [0 for i in range(len(pairs))]
		for l,(i,j) in enumerate(pairs):
			best_swap_for_pairs[l] = max( min(largest- nums[i],largest- nums[j]),
			     min(nums[i]- smallest, nums[j] - smallest) ,
			     abs(nums[i] - nums[j])
			     )
		print(min(best_swap_for_pairs))

solve()