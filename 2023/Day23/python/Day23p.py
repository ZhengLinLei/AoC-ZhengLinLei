import sys
sys.setrecursionlimit(10**6)
K, B='#', '.'; A=open('../in').read().strip().splitlines(); D, J=len(A), len(A[0])
def I(y,x,e_y,e_x,vv,length):
	O=length;N=vv;M=e_x;L=e_y
	if y==L and x==M:return O
	if(y,x)in N:return-1
	G=set(N);G.add((y,x));F=A[y][x]
	if F=='<':B=[(0,-1)]
	elif F=='>':B=[(0,1)]
	elif F=='^':B=[(-1,0)]
	elif F=='v':B=[(1,0)]
	else:B=[(-1,0),(1,0),(0,-1),(0,1)]
	H=[]
	for P in B:
		C,E=y+P[0],x+P[1]
		if C>=0 and E>=0 and C<D and E<J and A[C][E]!=K and(C,E)not in G:H.append((C,E))
	if not H:return-1
	return max(I(A,B,L,M,G,O+1)for(A,B)in H)
def N(y,x,e_y,e_x,vv,length):
	Q=length;P=e_x;O=e_y;L=vv
	if y==O and x==P:return Q
	if(y,x)in L:return-1
	L.add((y,x));R=[(-1,0),(1,0),(0,-1),(0,1)];M=[]
	for S in R:
		G=set(L);E,F=y+S[0],x+S[1]
		if E>=0 and F>=0 and E<D and F<J and A[E][F]!=K and(E,F)not in G:
			T=0;H,I=E,F
			while True:
				T+=1;U=[(H+A[0],I+A[1])for A in R];V=[];open=[]
				for(B,C)in U:
					if B>=0 and C>=0 and B<D and C<J and(B,C)not in G:
						if A[B][C]==K:V.append((B,C))
						else:open.append((B,C))
				if len(open)==1:G.add((H,I));H,I=open[0]
				else:break
			M.append((H,I,G,T))
	if not M:return-1
	return max(N(A,B,O,P,C,Q+D)for(A,B,C,D)in M)
def C(x):C=0;E=0,A[0].index(B);F=D-1,A[-1].index(B);C=I(E[0],E[1],F[0],F[1],set(),0) if x else N(E[0],E[1],F[0],F[1],set(),0);return(str(C))
print("Part 1: ", C(True), "\nPart 2 :", C(False));
