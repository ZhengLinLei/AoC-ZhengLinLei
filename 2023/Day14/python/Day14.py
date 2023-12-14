A=[list(A.strip())for A in open('../in')]
def J(lines):
	A=lines
	for F in range(len(A)):
		for B in range(1,len(A)):
			for E in range(len(A[B])):
				if A[B][E]=='O' and A[B-1][E]=='.':A[B][E],A[B-1][E]='.','O'
	return A
E={}
B,F=-1,1000000000
while(B:=B+1)<F:
	for K in range(4):A=list(map(list,zip(*J(A)[::-1])))
	B=F-(F-B)%(B-E[str(A)])if str(A)in E else B;E[str(A)]=B
print(sum([range.count('O')*(len(A)-B)for(B,range)in enumerate(A)]))