#!PY
# Path: ./

# Part 1 and 2
# Zheng Lin Lei


from functools import cache
from heapq import heappush, heappop

DIRS = {'<':(-1, 0), '>':(1, 0), '^':(0, -1) ,'v':(0, 1), '.':(0, 0)}
G_W, G_H = 0, 0

@cache
def step(grid, blizz):
    blizz = frozenset((((x+dx)%G_W, (y+dy)%G_H), (dx, dy)) for (x, y), (dx, dy) in blizz)
    free = grid - {b[0] for b in blizz}
    return blizz, free

def md(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def walk(start, goal, grid, blizzards):
    stack, seen, ti = [], set(), 0
    heappush(stack, (0, start, blizzards, ti))
    while stack:
        _, (x, y), blizz, t = heappop(stack)
        blizz, free = step(grid, blizz)
        for (dx, dy) in DIRS.values():
            p = (x+dx, y+dy)
            if p == goal:
                return t+1, blizz
            elif p in free:
                if (p, blizz) not in seen:
                    seen.add((p, blizz))
                    heappush(stack, (md(*p, *goal)+t, p, blizz, t+1))
    return -1

grid, blizzards = set(), set()
with open('./input.txt') as f:
    for y, row in enumerate(f.readlines()[1:-1]):
        G_H = max(y + 1, G_H)
        for x, val in enumerate(row.strip()[1:-1]):
            G_W = max(x + 1, G_W)
            grid.add((x, y))
            if val != '.': blizzards.add(((x, y), DIRS[val]))

start, goal = (0, -1), (G_W-1, G_H)
grid.add(start)
grid.add(goal)
tt = []
grid, blizz = frozenset(grid), frozenset(blizzards)
for p1, p2 in (start, goal), (goal, start), (start, goal):
    t, blizz = walk(p1, p2, grid, blizz)
    tt.append(t)
print('Part 1:', tt[0])
print('Part 2:', sum(tt))