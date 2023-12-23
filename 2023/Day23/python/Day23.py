G='.<>^v';A=tuple(open('../in').read().split('\n')); B=len(A[0]); C=len(A)
			
def E(tr,D,end):
	A=set([D]);B=[(D,0,A)];C=0
	while B:
		E,F,A=B.pop()
		if E==end:C=max(C,F)
		for(G,next)in tr[E]:
			if next not in A:B.append((next,F+G,A|set([next])))
	return C
def L(B,C,A):
	D=1
	while len(B[A])==2:D+=1;next=[A for(B,A)in B[A]if A!=C][0];C,A=A,next
	return D,A
def K(x,y):
	for(F,H)in((0,1),(1,0),(0,-1),(-1,0)):
		D,E=x+F,y+H
		if 0<=D<B and 0<=E<C:
			if A[E][D]in G:yield(D,E)
def D():
	D={}
	for E in range(C):
		for F in range(B):
			if A[E][F]in G:D[F,E]=[(1,A)for A in K(F,E)]
	H={}
	for(I,J)in D.items():
		if len(J)!=2:H[I]=[L(D,I,A[1])for A in J]
	return H

F=1,0
H=B-2,C-1
print(E(D(),F,H))