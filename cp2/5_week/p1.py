class Fenwick():
	def __init__(self, size): 
		self.tree = [0]* (size+1)
	def add(self, value, index):
		while index < len(self.tree):
			self.tree[index] += value
			index += index & (-index)
	def query(self, index):
		ret = 0
		while index > 0:
			ret += self.tree[index]
			index -= index & (-index)
		return ret
	def tp(self):
		print(self.tree)

def sol():
	(n,q) = map(int , input().split())
	fen = Fenwick(size = n)
	for i in range(q):
		line = input().split()
		if len(line) == 3:
			(index, value) = map(int , line[1:])
			fen.add(value, index+1)
		else:
			index = int(line[1])
			print(fen.query(index))
sol()
