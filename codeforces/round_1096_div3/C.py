#https://codeforces.com/contest/2227/problem/C
# assuming no number is | 6, each valid subarray starting at i where a[i] | 2
# at or after the first j where a[j] | 3. so seperate a[i] | 2 from a[j] | 3 with as much
# distance as possible. For sixes, just place them all on the left.
def solve():
	for _ in range(int(input())):
		_ = input()
		arr = list(map(int, input().split()))
		six_bag, two_bag, three_bag, other_bag = [], [] , [], []
		for i in arr:
			if i % 6 ==0:
				six_bag.append(i)
			elif i % 2 == 0:
				two_bag.append(i)
			elif i % 3 == 0:
				three_bag.append(i)
			else:
				other_bag.append(i)
		narr = six_bag + two_bag + other_bag + three_bag
		print(*narr)
solve()