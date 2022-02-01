# warning: minified
from struct import pack as H,error
def D(m,v,A=0):
	for B in range(len(m)):
		if v>>B&1:A^=m[B]
	return A
def I(K):
	F,B,C=K,{},0
	for A in F.values():B.setdefault(A,0);B[A]+=1;C=max(C,A)
	D,E={},0
	for A in range(C):E=E+B.get(A,0)<<1;D[A+1]=E
	G={}
	for (H,A) in sorted(F.items(),key=lambda x:(x[1],x[0])):G[H]=D[A],A;D[A]+=1
	return G
class P:
	def __init__(A):A.done=[];A.current=0;A.bit_pos=0
	def push(A,x,n):
		while n>=8-A.bit_pos:A.current|=x<<A.bit_pos&255;x>>=8-A.bit_pos;n-=8-A.bit_pos;A.done.append(A.current);A.current,A.bit_pos=0,0
		A.current|=x<<A.bit_pos&255;A.bit_pos+=n
	def push_rev(B,x,n):
		A=1<<n>>1
		while A:B.push(x&A and 1 or 0,1);A>>=1
	def bytes(A):
		B=bytes(A.done)
		if A.bit_pos:B+=bytes([A.current])
		return B
def make_zip(f,num_files,compressed_size):
	J,Q,F=num_files,[3988292384]+[1<<A for A in range(31)]+[1<<32],{0:2,1:3,2:3,18:1};K,R=I(F),{0:2,256:2,285:1};L,S,A=I(R),I({0:1}),P();A.push(1,1);A.push(2,2);A.push(29,5);A.push(0,5);T=16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15;U=max((T.index(A)for A in F))+1;A.push(U-4,4)
	for c in T[:U]:A.push(F.get(c,0),3)
	def V(E,D=0):
		for (G,H) in sorted(E.items()):
			B=G-D
			while B>=11:
				if B<138:C=B
				elif B<149 and F[18]<(B-138)*F[0]:C=B-11
				else:C=138
				A.push_rev(*K[18]);A.push(C-11,7);B-=C
			while B>0:A.push_rev(*K[0]);B-=1
			A.push_rev(*K[H]);D=G+1
	V(R);V({0:1});B=0;A.push_rev(*L[0]);B+=1;d=A.bit_pos%2;B+=(9-A.bit_pos)//2*258;W,A=A.bytes(),P()
	if d:A.push(*S[0])
	while A.bit_pos<=4:A.push_rev(*L[285]);A.push(*S[0]);B+=258
	A.push_rev(*L[256]);X=A.bytes();Y=compressed_size-len(W)-len(X);B+=Y*1032;e=W+b'\x00'*Y+X;Z=B;C=[1<<A for A in range(33)]
	for _ in range(8):C=[D([Q,[D(Q,A)for A in[1<<A for A in range(32)]+[(1<<32)+1]]][0],A)for A in C]
	M=[1<<A for A in range(33)]
	while B:
		if B&1:M=[D(M,A)for A in C]
		C=[D(C,A)for A in C];B>>=1
	N,B,E=e,B,0;a=D(M,8589934591)&4294967295^4294967295
	try:E+=f.write(H('<LHHHHHLLLHH',67324752,20,0,8,0,0,a,len(N),Z,1,0)+b'0')
	except error:raise ValueError()
	E+=f.write(N);b=E
	for G in range(J):
		O=[]
		while True:
			O.insert(0,b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[G%36]);G=G//36-1
			if G<0:break
		E+=f.write(H('<LHHHHHHLLLHHHHHLL',33639248,20,20,0,8,0,0,a,len(N),Z,len(bytes(O)),0,0,0,0,0,0)+bytes(O))
	f.write(H('<LHHHHLLH',101010256,0,0,J,J,E-b,b,0))