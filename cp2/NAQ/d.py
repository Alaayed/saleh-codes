states = [ 'D' , 'L' , 'U' , 'R']
maze = [[1 for _ in range(51)] for _ in range(51)]
visited= [[0 for _ in range(51)] for _ in range(51)]
goal = [-1,-1]
def carl_run(orient, r, c):
	if (r == goal[0] and c == goal[1]):
		print(1)
		exit()
	orient = orient % 4
	if ((visited[r][c] & orient) != 0):
		return 
	# add to visited
	visited[r][c] += 1 << orient
	# step 1 all cases
	if (orient == 3 and maze[r+1][c] != 1):
		carl_run(orient-1, r+1, c)
	elif(orient == 2 and maze[r][c-1] != 1):
		carl_run (orient-1, r , c-1)
	elif(orient == 1 and maze[r-1][c] != 1):
		carl_run (orient-1, r-1, c)
	elif(orient == 0 and maze[r][c+1] != 1):
		carl_run(orient-1, r,c+1)
	# step 2 all cases
	if (orient == 3 and maze[r][c+1] != 1):
		carl_run(orient, r, c+1)
	elif(orient == 2 and maze[r+1][c] != 1):
		carl_run (orient, r+1 , c)
	elif(orient == 1 and maze[r][c-1] != 1):
		carl_run (orient, r, c-1)
	elif(orient == 0 and maze[r-1][c] != 1):
		carl_run(orient, r-1,c)
	# step 3 
	carl_run (orient+1, r, c)

def solve():
	(r,c) = map(int, input().split())
	(sr,sc) = map(int, input().split())
	(er,ec) = map(int, input().split())
	goal[0] = er
	goal[1] = ec
	for i in range(r):
		line = list(map (int , list(input())))
		for j,c in enumerate(line):
			maze[i+1][j+1] = c

	carl_run (3, sr, sc)
	print(0)
solve()
