# Part 1 and Part 2
# Zheng Lin Lei

input=[A.split()for A in open('../in').read().split('\n')]
hands=[A[0]for A in input]
bids=[A[1]for A in input]

def scoreO(hand):
	E=hand;I=0
	if vals[-1]=='J':
		counts.append([(str(E).count(A),A)for A in vals[:-1]]);B=0;counts[-1].append((0,'J'));B=counts[-1].index(max(counts[-1]))
		for H in E: 
			if H=='J':counts[-1][B]=counts[-1][B][0]+1,counts[-1][B][1]
	else:counts.append([(str(E).count(A),A)for A in vals])
	A,C,F,G=0,0,0,0
	for D in counts[-1]:
		if D[0]==2:A+=1
		if D[0]==3:C+=1
		if D[0]==4:F+=1
		if D[0]==5:G+=1
	if A+C+F+G==0:return 0
	if A==1:
		if C==1:return 4
		else:return 1
	if A==2:return 2
	if C==1:
		if A==1:return 4
		else:return 3
	if F==1:return 5
	if G==1:return 6
	
vals=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
counts=[]; scores=[]
for i in range(len(hands)):hand=hands[i];scores.append((hand,bids[i],scoreO(hands[i]),counts[i]))
# Sorting
scores.sort(key=lambda x:[x[-1][A][0]for A in range(13)])
scores.sort(key=lambda x:vals.index(x[0][4]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][3]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][2]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][1]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][0]),reverse=True)
scores.sort(key=lambda x:x[-2])
somme=sum([int(A[1])*(scores.index(A)+1)for A in scores])
print('Part 1 : ',somme)

# ----

vals=['A','K','Q','T','9','8','7','6','5','4','3','2','J']
counts=[]
scores=[]
for i in range(len(hands)):hand=hands[i];scores.append((hand,bids[i],scoreO(hands[i]),counts[i]))
# Sorting
scores.sort(key=lambda x:[x[-1][A][0]for A in range(13)])
scores.sort(key=lambda x:vals.index(x[0][4]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][3]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][2]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][1]),reverse=True)
scores.sort(key=lambda x:vals.index(x[0][0]),reverse=True)
scores.sort(key=lambda x:x[-2])
somme=sum([int(A[1])*(scores.index(A)+1)for A in scores])
print('Part 2 : ',somme)