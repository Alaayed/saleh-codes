def solve():
	string = input()
	letters = [0 for _ in range(26)]
	for s in string:
		letters[ord(s)-ord('a')] += 1
	letters = [1 if l != 0 else 0 for l in letters]
	res = 'CHAT WITH HER!' if sum(letters) % 2 == 0 else 'IGNORE HIM!'
	print(res)
solve()