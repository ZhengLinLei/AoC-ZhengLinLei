from collections import deque
G=open('../in').read().strip(); K=G.split('\n'); E=[[A for A in A]for A in K]; B=len(E); C=len(E[0])
for D in range(B):
	for F in range(C):
		if E[D][F]=='S':H,I=D,F
def M(r,c):
	F={};G=deque([(0,0,H,I,0)])
	while G:
		A,D,r,c,J=G.popleft()
		if r<0:A-=1;r+=B
		if r>=B:A+=1;r-=B
		if c<0:D-=1;c+=C
		if c>=C:D+=1;c-=C
		if not(0<=r<B and 0<=c<C and E[r][c]!='#'):continue
		if(A,D,r,c)in F:continue
		if abs(A)>4 or abs(D)>4:continue
		F[A,D,r,c]=J
		for(K,L)in[[-1,0],[0,1],[1,0],[0,-1]]:G.append((A,D,r+K,c+L,J+1))
	return F
G=M(H,I)
A={}
def L(d,v,L):
	E=(L-d)//B
	if(d,v,L)in A:return A[d,v,L]
	C=0
	for D in range(1,E+1):
		if d+B*D<=L and(d+B*D)%2==L%2:C+=D+1 if v==2 else 1
	A[d,v,L]=C;return C
def J(part1):
	M=part1;D=64 if M else 26501365;E=0
	for J in range(B):
		for K in range(C):
			if(0,0,J,K)in G:
				def N(tr,tc):
					E=tc;D=tr;F=0;A=3
					if D>A:F+=B*(abs(D)-A);D=A
					if D<-A:F+=B*(abs(D)-A);D=-A
					if E>A:F+=C*(abs(E)-A);E=A
					if E<-A:F+=C*(abs(E)-A);E=-A
					F+=G[D,E,J,K];return F
				A=[-3,-2,-1,0,1,2,3]
				for F in A:
					for H in A:
						if M and(F!=0 or H!=0):continue
						I=G[F,H,J,K]
						if I%2==D%2 and I<=D:E+=1
						if F in[min(A),max(A)]and H in[min(A),max(A)]:E+=L(I,2,D)
						elif F in[min(A),max(A)]or H in[min(A),max(A)]:E+=L(I,1,D)
	return E
print('Part 1: ', J(True))
print('Part 2: ', J(False))
