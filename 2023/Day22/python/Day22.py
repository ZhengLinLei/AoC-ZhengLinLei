# Part 1 and Part 2
# Zheng Lin Lei

import re
from collections import defaultdict as G
def M(s):return list(map(int,re.findall('\\d+',s))) # Or use it from util.py
N=[tuple(M(B)+[A])for(A,B)in enumerate(open('../in').read().strip().split('\n'))]
def E(brv):A=brv;return A[0],A[1],A[2]-1,A[3],A[4],A[5]-1,A[6]
def D(brv):
	A=brv
	for B in range(A[0],A[3]+1):
		for C in range(A[1],A[4]+1):
			for D in range(A[2],A[5]+1):yield(B,C,D)
C={}
F=[]
for A in sorted(N,key=lambda brv:brv[2]):
	while A[2]>0 and all(A not in C for A in D(E(A))):A=E(A)
	for B in D(A):C[B]=A
	F.append(A)
H=G(set)
I=G(set)
for A in F:
	O=set(D(A))
	for B in D(E(A)):
		if B in C and B not in O:H[C[B]].add(A);I[A].add(C[B])
def P(ded):
	A=set()
	def C(brv):
		B=brv
		if B in A:return
		A.add(B)
		for D in H[B]:
			if not len(I[D]-A):C(D)
	C(ded);return len(A)
J=0
K=0
for A in F:L=P(A);J+=L==1;K+=L-1
print("Part 1: ", J, "\nPart 2: ", K)