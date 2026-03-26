class StringHashing:
	def __init__(self, s):
		self.s = s
		self.n = len(s)
		n = len(s)
		self.mod1 = 10 ** 9 + 7
		self.mod2 = 10 ** 9 + 9

		self.base = 131

		self.h1 = [0] * (n + 1)
		self.h2 = [0] * (n + 1)
		self.p1 = [1] * (n + 1)
		self.p2 = [1] * (n + 1)

		for i in range(n):
			self.h1[i + 1] = (self.h1[i] * self.base + ord(s[i])) % self.mod1
			self.h2[i + 1] = (self.h2[i] * self.base + ord(s[i])) % self.mod2
			self.p1[i + 1] = (self.p1[i] * self.base) % self.mod1
			self.p2[i + 1] = (self.p2[i] * self.base) % self.mod2

	def get_hash(self, l, r):
		"""Returns hash of s[l:r] (0-indexed, exclusive r)."""
		h1 = (self.h1[r] - self.h1[l] * self.p1[r - l]) % self.mod1
		h2 = (self.h2[r] - self.h2[l] * self.p2[r - l]) % self.mod2
		return (h1, h2)

	def equal(self, l1, r1, l2, r2):
		"""True if s[l1:r1] == s[l2:r2]."""
		return self.get_hash(l1, r1) == self.get_hash(l2, r2)
