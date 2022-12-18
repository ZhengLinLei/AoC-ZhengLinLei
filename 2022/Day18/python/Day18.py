# Part 1 and 2

# Zheng Lin Lei
from collections import deque
import re

cubes = set(map(eval,re.findall('\d+,\d+,\d+', open('../input.txt').read())))
block = {(a,b,c) for a in range(-1, 21) for b in range(-1, 21) for c in range(-1, 21)}-cubes
delta = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
sides = lambda x,y,z: {(x+a,y+b,c+z) for a,b,c in delta} & block
steam = set()
nodes = deque([(-1,-1,-1)])
while nodes:
    n = nodes.pop()
    steam.add(n)
    nodes.extend(sides(*n)-steam)
print('Part 1: ', sum(len(sides(*c)-cubes) for c in cubes))
print('Part 2: ', sum(len(sides(*c)&steam) for c in cubes))