# Part 1 and 2: 2022/Day20/python/Day20.py

# Zheng Lin Lei


from __future__ import annotations
from random import random
from dataclasses import dataclass
from math import log2, ceil

s = open("../input.txt").read()
a = list(map(int, s.splitlines()))
n = len(a)

MAXLEVEL = int(ceil(log2(n)))

@dataclass
class Link:
    dist: int
    target: Node

def randlvl():
    for i in range(1, MAXLEVEL):
        if random() < .5:
            return i
    return MAXLEVEL

class Node:
    def __init__(self, v) -> None:
        self.v = v
        lvl = randlvl()
        self.nexts = [Link(1, self) for _ in range(lvl)]
        self.prevs = [Link(1, self) for _ in range(lvl)]

    def height(self):
        return len(self.nexts)

    def new_after(self, v) -> Node:
        """Create a new node after this node"""
        return Node(v).insert_after(self)

    def insert_after(self, anchor: Node) -> Node:
        """Place this floating node after anchor"""
        for i, ((dprv, prv), (dnxt, nxt)) in enumerate(zip(anchor.climb(True), anchor.nexts[0].target.climb(False))):
            if i < self.height():
                self.prevs[i] = Link(1+dprv, prv)
                self.nexts[i] = Link(1+dnxt, nxt)
                prv.nexts[i] = Link(1+dprv, self)
                nxt.prevs[i] = Link(1+dnxt, self)
            else:
                prv.nexts[i].dist += 1
                nxt.prevs[i].dist += 1
        return self

    def forward(self, dist: int) -> Node:
        it = self
        while dist > 0:
            for link in reversed(it.nexts):
                if dist - link.dist >= 0:
                    dist -= link.dist
                    it = link.target
                    break
        return it
    
    def move_after(self, anchor: Node):
        """Move this node after another node in the same list"""
        if anchor is self:
            return
        for i, ((dprv, prv), (dnxt, nxt)) in enumerate(zip(self.prevs[0].target.climb(True), self.nexts[0].target.climb(False))):
            if i < self.height():
                prv.nexts[i] = Link(1+dprv+dnxt, self.nexts[i].target)
                nxt.prevs[i] = Link(1+dprv+dnxt, self.prevs[i].target)
            else:
                prv.nexts[i].dist = nxt.prevs[i].dist = 1+dprv+dnxt
        self.insert_after(anchor)

    def side(self, prev: bool):
        return self.prevs if prev else self.nexts
        
    def climb(self, prev: bool):
        d = 0
        it = self
        for i in range(MAXLEVEL):
            orig = it
            while i >= it.height():
                d += it.side(prev)[i-1].dist
                it = it.side(prev)[i-1].target
                if it is orig:
                    return
            yield d, it

for mult, rounds in [(1, 1), (811589153, 10)]:
    head = Node(a[0] * mult)
    nodes = [head]
    nodes.extend(nodes[-1].new_after(x*mult) for x in a[1:])
    n0 = nodes[a.index(0)]
    for _ in range(rounds):
        for node in nodes:
            anchor = node.forward(node.v % (n-1))
            node.move_after(anchor)

    print(sum(n0.forward(x).v for x in (1000, 2000, 3000)))