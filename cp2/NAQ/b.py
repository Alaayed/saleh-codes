from collections import deque
grid = [ [ 0 for _ in range(501)]  for _ in range(501)]

for i in range(501):
	grid[i][0] = [-1,0]
	grid[i][500]=[-1,0]
for j in range(501):
	grid[0][j] = [-1,0]
	grid[500][j]=[-1,0]

def solve():
	(r,c,n) = map(int, input().split())
	queue = deque()
	towers = [ [-1, -1]]
	for i in range(n):
		(j,k) = map(int , input().split())
		queue.appendleft(  [i+1, j, k] )
		towers.append([j, k])
	
	while queue:
		(i , j , k) = queue.pop()
		if grid[j][k][0] == -1: # out of bounds
			continue
		if grid[j][k][0] == 0:
			grid[j][k][0] = i
		elif grid[j][k][1] == 0:
			grid[j][k][1] = i
		else:
			continue
		queue.appendleft( (i , j + 1, k))
		queue.appendleft( (i , j - 1, k))
		queue.appendleft( (i , j, k+1))
		queue.appendleft( (i , j, k-1))
	for i, row in enumerate(grid[1:]):
		if i == r:
			break
		row_str = ""
		l_str = ""
		for (a, b) in row[1:(c+1)]:
			row_str += str(a) + " "
			l_str += str(b) + " "

		print(row_str)



solve()
