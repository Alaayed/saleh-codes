#https://codeforces.com/contest/2227/problem/D
# Any correct solution must contain zero
# it is therefor either centered at one of the two zeros
# or contains both zeros.
def mex(a):
	n = len(a)
	f = [0] * (n+1)
	for i in a:
		if i <= n: f[i] = 1
	mex = 0
	while f[mex] != 0: mex+=1
	return mex
def is_palindrome(s, l, r):
	n = len(s)
	while l <= n-1 and 0 <= r and l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

def find_palindrome_ends(s, l, r):
	"""
	function contract, s[l:r+1] is a palindrome
	:param s: arr to compare
	:param l: left endpoint
	:param r: right endpoint
	:return: the largest superset of current palindrome
	"""
	while l >= 0 and r <= len(s)-1:
		if s[l] != s[r]:
			return l+1, r-1
		l -=1
		r +=1
	return l+1, r-1
def solve():
	for _ in range(int(input())):
		n = int(input())
		cmex = -1
		arr = list(map(int, input().split()))
		# find the first and second zeros
		i = arr.index(0)
		j = arr.index(0, i+1)

		# centered at i
		l,r = find_palindrome_ends(arr, i, i)
		cmex = max(mex(arr[l:r+1]), cmex)
		# center at j
		l, r = find_palindrome_ends(arr, j, j)
		cmex = max(mex(arr[l:r + 1]), cmex)
		# i through j
		if is_palindrome(arr, i, j):
			l, r = find_palindrome_ends(arr, i, j)
			cmex = max(mex(arr[l:r + 1]), cmex)
		print(cmex)



solve()