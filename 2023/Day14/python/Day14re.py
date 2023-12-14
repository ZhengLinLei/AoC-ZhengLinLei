# Part 1 and Part 2
# Zheng Lin Lei
import numpy as np

dd = open("../in").read().splitlines()
d = np.array([list(x) for x in dd])


def A(arr):
	B=True
	while B:
		B=False
		for(nd,F)in enumerate(arr[:-1]):
			for(C,G)in enumerate(F):
				if G=='.'and arr[nd+1][C]=='O':F[C]='O';arr[nd+1][C]='.';B=True
	return arr

def B(arr):
	for _ in range(4):arr=A(arr);arr=np.rot90(B,k=1,axes=(1,0))
	return B
def C(arr): A=arr;A=np.rot90(A,axes=(1,0));return sum(sum(A+1 for(A,B)in enumerate(A)if B=='O')for A in A)


nd = d.copy()
print("Part 1:", C(A(nd)))

hh = []
T = 0
while True:
	G=[''.join(A)for A in list(nd)];A=hash(tuple([''.join(A)for A in list(nd)]))
	if A in hh and not D:C=hh.index(A);F=len(hh)-C;D=(1000000000-C)%F+C+F
	if T and len(hh)==T:break
	hh.append(A);nd=B(nd)

print("Part 2:", C(nd))