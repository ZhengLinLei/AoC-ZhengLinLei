# Part 1
# Zheng Lin Lei
C,H=[],0
for M in open('../in'):N,O=M.strip().split(' @ ');P,Q,R=N.split(', ');S,T,U=O.split(', ');C.append((int(P),int(Q),int(R),int(S),int(T),int(U)))
for I in range(len(C)-1):
	A=C[I];E=A[4]/A[3];F=A[1]-E*A[0]
	for V in range(I+1,len(C)):
		B=C[V];G=B[4]/B[3];J=B[1]-G*B[0]
		if E==G:
			if F==J:exit()
			continue
		D=(J-F)/(E-G);K=E*D+F;W=(D-A[0])/A[3];X=(D-B[0])/B[3]
		if W>=0 and X>=0 and D>=0xb5e620f48000 and D<=0x16bcc41e90000 and K>=0xb5e620f48000 and K<=0x16bcc41e90000:H+=1
print("Part 1: ", H)