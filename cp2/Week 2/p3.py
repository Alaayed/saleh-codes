import bisect
def intersecting_rectangles():
	n = int( input() )
	rectangles = [tuple(map(int, input().split())) for _ in range(n)]
	start_event, end_event = create_segments(rectangles)
	start_event.sort()
	end_event.sort()
	hseg = []
	score, s1, e1 = 0 , 0 , 0
	while s1 != len(start_event) and e1 != len(end_event):
		if start_event[s1][0] < end_event[e1][0]:
			x, y1 , y2 = start_event[s1]
			s1+=1
			# Process vertical segement
			score += num_in_range(hseg, y1, y2)
			# add hseg
			bisect.insort(hseg, y1)
			bisect.insort(hseg, y2)
		else:
			x, y1 , y2 = end_event[e1]
			e1+=1
			# remove rectangles vertical segments
			hseg.remove(y1)
			hseg.remove(y2)
			# process score
			score += num_in_range(hseg, y1, y2)
		if score != 0:
			return 1
	return score // 2

def create_segments(rectangles):
	start_event = []
	end_event = []
	for x1, y1 , x2 , y2 in rectangles:
		start_event.append( ( x1 , y1 , y2) )
		end_event.append( ( x2, y1 , y2 ) )
	return start_event, end_event
def num_in_range(hseg, y1 , y2):
	return abs(bisect.bisect(hseg, y1) - bisect.bisect(hseg, y2))
print(intersecting_rectangles())