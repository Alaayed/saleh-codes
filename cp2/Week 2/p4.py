def duel_cards():
	n = int(input())
	alice_cards = [ int(input()) for _ in range(n) ]
	possible_cards = [i+1 for i in range(2*n)]
	bobs_cards = list(set(possible_cards) - set(alice_cards))
	alice_cards.sort()
	bobs_cards.sort()
	max_points = duel(c1= alice_cards.copy(), c2= bobs_cards.copy())
	min_points = n-duel(c1 =bobs_cards, c2=alice_cards)
	print(f'{min_points} {max_points}')
def duel(c1 , c2):
	# win for c1
	points = 0
	while c1 and c2:
		if c1[-1] > c2[-1]:
			c1.pop()
			c2.pop()
			points +=1
		elif c1[-1] < c2[-1]:
			c2.pop()
	return points
duel_cards()
