def build_z(s):
	n = len(s)
	z = [0] * n
	l = r = 0
	for i in range(1, n):
		if i < r:
			z[i] = min(r - i, z[i - l])
		while i + z[i] < n and s[z[i]] == s[i + z[i]]:
			z[i] += 1
		if i + z[i] > r:
			l, r = i, i + z[i]
	return z


def z_search(text, pat):
	"""
	Returns all start indices (0-indexed) where pat occurs in text.
	Classic trick: build Z on  pat + '$' + text,
	then any position i where z[i] == len(pat) is a match.
	"""
	if not pat:
		return []
	m = len(pat)
	s = pat + "$" + text
	z = build_z(s)
	offset = m + 1
	return [i for i in range(len(text)) if z[offset + i] == m]
