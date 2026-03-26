import math
def solve(k):
	mappings = {}
	for _ in range(k):
		category = input().split()[-1]
		mappings[category] = mappings.get(category, 1) + 1
	print(math.prod( mappings.values() )-1)
def read_in():
	n = int(input())
	for _ in range(n):
		k = int(input())
		solve(k)
read_in()
