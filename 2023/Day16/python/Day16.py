# Part 1 and Part 2
# Zheng Lin Lei
g = {i+j*1j: c for j, r in enumerate(open('../in')) for i, c in enumerate(r.strip())}

def A(x,y):
	C=set([(x,y)]);E=set()
	while C:
		B,A=C.pop()
		while not(B,A)in E:
			E.add((B,A));B+=A
			match g.get(B):
				case'-':A=1;C.add((B,-A))
				case'|':A=1j;C.add((B,-A))
				case'/':A=-complex(A.imag,A.real)
				case'\\':A=complex(A.imag,A.real)
				case None:break
	return len(set(A for(A,B)in E))-1

print("Part 1: ", A(-1, 1))

print("Part 2: ", max(map(A, *zip(*[(p-d, d) for p in g for d in (1,1j,-1,-1j) if p-d not in g]))))