R = open('../in').read().strip();A=0,0;E=0;F=0;M=0;B=0,0;G=0;H=0;N=0
for S in R.split('\n'):
	T,U,V=S.split()
	match T:
		case'L':C=-1,0
		case'R':C=1,0
		case'U':C=0,-1
		case'D':C=0,1
	I=int(U);J=A[0]+C[0]*I,A[1]+C[1]*I;E=E+A[0]*J[1];F=F+A[1]*J[0];M+=I;A=J;O=V.removeprefix('(#').removesuffix(')');K=int(O[:5],base=16)
	match O[5]:
		case'0':D=1,0
		case'1':D=0,1
		case'2':D=-1,0
		case'3':D=0,-1
	L=B[0]+D[0]*K,B[1]+D[1]*K;G=G+B[0]*L[1];H=H+B[1]*L[0];N+=K;B=L
	
W=abs(E-F)/2
print("Part 1:", int(W+M/2+1))
X=abs(G-H)/2
print("Part 2:", int(X+N/2+1))