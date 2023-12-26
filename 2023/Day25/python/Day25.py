# Part 1
import collections as F
B=F.defaultdict(set)
for G in open('../in'):
	C,*H=G.replace(':','').split()
	for D in H:B[C].add(D);B[D].add(C)
A=set(B)
E=lambda v:len(B[v]-A)
while sum(map(E,A))!=3:A.remove(max(A,key=E))
print("Part 1: ", len(A)*len(set(B)-A))