from collections import defaultdict as J
from math import prod as K
E=dict()
L=J(int)
C=J(dict)
for Q in open('../in'):
	A,X,*M=Q.replace(',','').split();R,A=(A[0],A[1:])if A[0]in'%&'else('',A);E[A]=R,M
	for N in M:
		C[N][A]=0
		if N=='rx':S=A
F={A:0 for A in C[S]}
G=0
O=[0,0]
while True:
	if G==1000:print('Part 1:',K(O))
	G+=1
	if all(F.values()):print('Part 2:',K(F.values()));break
	H=[(None,'broadcaster',0)]
	while H:
		T,B,D=H.pop(0);O[D]+=1
		if B not in E:continue
		type,P=E[B]
		match(type,D):
			case'',_:I=D
			case'%',0:I=L[B]=not L[B]
			case'&',_:
				C[B][T]=D;I=not all(C[B].values())
				if'rx'in P:
					for(U,V)in C[B].items():
						if V:F[U]=G
			case _,_:continue
		for W in P:H.append((B,W,I))