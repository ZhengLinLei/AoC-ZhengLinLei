# Zheng Lin Lei
# Part 1 and Part 2

times, distances = map(lambda x: x.split()[1:], open('../in').read().split('\n'))
ways = 1
for i in range(len(times)):
    t = int(times[i]); d = int(distances[i])
    w = 0
    for i in range(1, t):
        if (i * (t-i)) > d:
            w += 1
    ways *= w

print("Part 1", ways)

t = int(''.join(times)); d = int(''.join(distances))
ways = 0
for i in range(1, t):
  if (i * (t-i)) > d:
    ways += 1

print("Part 2", ways)

