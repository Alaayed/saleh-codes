from math import ceil
# Key property: It's ALWAYS optimal to move the apples one step further
# Intuitive proof, you are always "paying" for each apple every kilo
# Lets assume an optimal solution exists
# Where we move n apples from i to j with a sack k where j-i > 1
# and for each apple, the cost to move it from i to j in one trip
# is the SAME to move it from i to j in j-i trips
# so the dp solution will look like dp[i+1] = dp[i] - ceil((dp[i] // k))
# ceil to account for when n % k != 0, because we always
# move all apples forward
# ex: n=9, k = 4
# first trip takes 4, second takes 4, last takes 1
# f1 = 3, f2= 3, f3 = 0, = dp[i+1] = 9-3 = 6
def apple_sack():
	line= [int(s) for s in input().split(sep=' ')]
	n,k = line[0], line[1]
	dp=[0 for _ in range(n+1)]
	# base case
	if n == 0:
		return 1
	dp[0]=n
	for i in range(1,n+1):
		dp[i] = dp[i-1] - ceil(dp[i-1]/k)
		if dp[i] == 0:
			return i+1
	return -1
print(apple_sack())