import functools, time

ll = [x for x in open("../in").read().strip().split('\n')]


@functools.lru_cache(maxsize=None)
def solve(s, wr, remain):
	if not s:
		if wr is None and len(remain) == 0:
			return 1
		if len(remain) == 1 and wr is not None and wr == remain[0]:
			return 1
		return 0
	possibleMore = 0
	for ch in s:
		if ch == '#' or ch == '?':
			possibleMore += 1
	if wr is not None and possibleMore + wr < sum(remain):
		return 0
	if wr is None and possibleMore < sum(remain):
		return 0
	if wr is not None and len(remain) == 0:
		return 0
	poss = 0
	if s[0] == '.' and wr is not None and wr != remain[0]:
		return 0
	if s[0] == '.' and wr is not None:
		poss += solve(s[1:], None, remain[1:])
	if s[0] == '?' and wr is not None and wr == remain[0]:
		poss += solve(s[1:], None, remain[1:])
	if (s[0] == '#' or s[0] == '?') and wr is not None:
		poss += solve(s[1:], wr+1, remain)
	if (s[0] == '?' or s[0] == '#') and wr is None:
		poss += solve(s[1:], 1, remain)
	if (s[0] == '?' or s[0] == '.') and wr is None:
		poss += solve(s[1:], None, remain)
	return poss

p1 = 0
p2 = 0

start = time.time()
for l in ll:
	s = l.split(" ")[0]
	v = tuple([int(x) for x in l.split(" ")[1].split(",")])
	p1 += solve(s, None, v)
	news = ""
	for j in range(5):
		news += "?"
		news += s
	p2 += solve(news[1:], None, v*5)

print("Time (ms): ", (time.time() - start)*1000)
print("Part 1: ", p1, "\nPart 2: ", p2)
