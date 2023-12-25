# Part 2
# Zheng Lin Lei

import re
import numpy as np
O=open('../in').read().splitlines()
R,S=0xb5e620f48000,0x16bcc41e90000
A=[[int(A)for A in re.findall('-?[0-9]+',A)]for A in O]
def H(x1,y1,dx1,dy1,x2,y2,dx2,dy2):return[dy2-dy1,dx1-dx2,y2-y1,x2-x1],y1*dx1-y2*dx2+x2*dy2-x1*dy1
I=min([B for A in A[:8]for B in A[:3]])
for B in range(8):
	for P in range(3):A[B][P]-=I
J,K,L,M,T=[],[],[],[],[]
for B in range(0,8,2):D,E=H(*A[B][:2]+A[B][3:5],*A[B+1][:2]+A[B+1][3:5]);J.append(D);L.append(E);D,E=H(*[A[B][0],A[B][2],A[B][3],A[B][5]],*[A[B+1][0],A[B+1][2],A[B+1][3],A[B+1][5]]);K.append(D);M.append(E)
F=np.array(J);G=np.array(L);N=np.linalg.solve(F,G);F=np.array(K);G=np.array(M);Q=np.linalg.solve(F,G)

print("Part 2: ", round(N[0])+round(N[1])+round(Q[1])+3*I)