def build_fail(p):
	m = len(p)
	f = [0] * m
	j = 0
	for i in range(1, m):
		while j > 0 and p[i] != p[j]:
			j = f[j - 1]
		if p[i] == p[j]:
			j += 1
		f[i] = j
	return f

# def build_fail(pattern):
#     m = len(pattern)
#     fail = [0] * m
#     prefix_len = 0
#     for i in range(1, m):
#         while prefix_len > 0 and pattern[i] != pattern[prefix_len]:
#             prefix_len = fail[prefix_len - 1]
#         if pattern[i] == pattern[prefix_len]:
#             prefix_len += 1
#         fail[i] = prefix_len
#     return fail
#
# Returns all start indices (0-indexed) where pat occurs in text.
def kmp_search(text, pat):
	if not pat:
		return []
	f = build_fail(pat)
	matches = []
	n, m = len(text), len(pat)
	j = 0
	for i in range(n):
		while j > 0 and text[i] != pat[j]:
			j = f[j - 1]
		if text[i] == pat[j]:
			j += 1
		if j == m:
			matches.append(i - m + 1)
			j = f[j - 1]
	return matches

