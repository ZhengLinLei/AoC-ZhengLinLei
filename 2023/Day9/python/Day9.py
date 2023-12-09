# Part 1
# Zheng Lin Lei

d=open('../in').read().splitlines()
def x(d):
 if all(x == 0 for x in d): return 0
 f=x([b-a for a,b in zip(d,d[1:])]);return d[-1]+f
print("Part 1:", sum([x(list(map(int, r.split())))for r in d]))