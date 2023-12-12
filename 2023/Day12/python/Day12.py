L=print
G=len
E='?'
A=None
import functools as M,time as C
N=[A for A in open('../in').read().strip().split('\n')]
@M.lru_cache(maxsize=A)
def D(s,wr,remain):
	J='.';I='#';C=remain;B=wr
	if not s:
		if B is A and G(C)==0:return 1
		if G(C)==1 and B is not A and B==C[0]:return 1
		return 0
	H=0
	for K in s:
		if K==I or K==E:H+=1
	if B is not A and H+B<sum(C):return 0
	if B is A and H<sum(C):return 0
	if B is not A and G(C)==0:return 0
	F=0
	if s[0]==J and B is not A and B!=C[0]:return 0
	if s[0]==J and B is not A:F+=D(s[1:],A,C[1:])
	if s[0]==E and B is not A and B==C[0]:F+=D(s[1:],A,C[1:])
	if(s[0]==I or s[0]==E)and B is not A:F+=D(s[1:],B+1,C)
	if(s[0]==E or s[0]==I)and B is A:F+=D(s[1:],1,C)
	if(s[0]==E or s[0]==J)and B is A:F+=D(s[1:],A,C)
	return F
F=0
H=0
O=C.time()
for I in N:
	J=I.split(' ')[0];K=tuple([int(A)for A in I.split(' ')[1].split(',')]);F+=D(J,A,K);B=''
	for P in range(5):B+=E;B+=J
	H+=D(B[1:],A,K*5)
L('Time (ms): ',(C.time()-O)*1000)
L('Part 1: ',F,'\nPart 2: ',H)