# link: https://codeforces.com/contest/2188/problem/D

# Okay, first step, start from the top
# If both x and y have a bit set pick either.
# x ^ y gives you the non contensious bits
# x & y gives you the conteded bits
# just loop through the contended bits and pick the one that minimizes the diff?
# seems right
def gain(x,p,i):
	return abs( x - (p)) -abs( x - (p | (1 << i)))

def get_score (x,p):
	return abs(x-p)
def get_dpscore(x,y,dp,j,i):
	return min(get_score(x,dp[j][0] | (1<< i) ) + get_score(y,dp[j][1] ),
	           get_score(x,dp[j][0]) + get_score(y,dp[j][1] | (1 <<i)))
def solve():
	for _ in range(int(input())):
		x,y = map(int,input().split())
		p = 0
		q = 0
		for i in reversed(range(31)):
			xg,yg = gain(x, p, i), gain(y, q, i)
			if xg > yg and xg >= 0:
				p |= 1 << i
			elif yg > xg and yg>= 0:
				q |= 1 << i
		print(p,q, abs(x-p) + abs(y-q))

def solve2():
	for _ in range(int(input())):
		x,y = map(int,input().split())
		p = 0
		q = 0
		# dp[i][2]
		# given the first i bits, ASSUMING i MUST set i,
		# what values p,q minimize the difference?
		dp = [ [0,0] for _ in range(32) ]
		for i in range(1, 31):
			curp, curq = 1 << (i-1), 1 << (i-1)
			current_score = abs(x-p) + abs(y-q)
			for j in range(i):
				if get_dpscore(x,y,dp,j, i-1) < current_score:
					curp = dp[j][0] | (1<<i-1)
					curq = dp[j][1] | (1<<i-1)
					current_score = abs(x-p) + abs(y-q)
			dp[i][0]=curp
			dp[i][1]=curq
		print(*min( [[abs(x-p) + abs(y-q),x,y] for p,q in dp])[1:])



solve2()