F = False; A = print; E = range; D = int; B = min
from math import log10,ceil
G=open('../in').read().split('\n')
def C(maps,seed):
	A=seed
	for C in maps:
		for(D,B,E)in C:
			if B<=A<B+E:A=D+(A-B);break
	return A
def H(seed_ranges=F):
	A=[D(A)for A in G[0].split(': ')[1].split(' ')]
	if seed_ranges: A=[(A[2*B],A[2*B+1])for B in E(len(A)//2)]
	C=[];B=[]
	for F in G[3:]:
		if F=='':continue
		if':'in F:C+=[B];B=[]
		else:B+=[tuple(D(A)for A in F.split(' '))]
	C+=[B];return A,C

def part1():
	A, D = H(seed_ranges = F)
	E = {C(D, A):A for A in A}
	G = B(E.keys())
	return G
def part2():
	I, J = H(seed_ranges = True)
	A = D(pow(10, ceil(log10(max(A[1] for A in I)/100))))
	F = {(B, B+D, F): C(J, F) for(B, D) in I for F in E(B, B+D ,A)}
	K = B(F.items(),key = lambda x: x[1]); L, M, G = K[0]
	while A>1: N= max(G-A,L);O=B(G+A,M);A=A//10;F={A:C(J,A)for A in E(N,O,A)};G,P=B(F.items(),key=lambda x:x[1])
	return P
A('Part 1:', part1())
A('Part 2:', part2())