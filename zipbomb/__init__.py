# warning: minified
from struct import pack as J,error
def E(m,v):
	A=0
	for B in range(len(m)):
		if v>>B&1:A^=m[B]
	return A
def K(K):
	F=K;B,C={},0
	for (I,A) in F.items():B.setdefault(A,0);B[A]+=1;C=max(C,A)
	D,E={},0
	for A in range(C):E=E+B.get(A,0)<<1;D[A+1]=E
	G={}
	for (H,A) in sorted(F.items(),key=lambda x:(x[1],x[0])):G[H]=D[A],A;D[A]+=1
	return G
class S:
	def __init__(A):A.done=[];A.current=0;A.bit_pos=0
	def push(A,x,n):
		while n>=8-A.bit_pos:A.current|=x<<A.bit_pos&255;x>>=8-A.bit_pos;n-=8-A.bit_pos;A.done.append(A.current);A.current=0;A.bit_pos=0
		A.current|=x<<A.bit_pos&255;A.bit_pos+=n
	def push_rev(B,x,n):
		A=1<<n>>1
		while A>0:B.push(x&A and 1 or 0,1);A>>=1
	def bytes(A):
		B=bytes(A.done)
		if A.bit_pos:B+=bytes([A.current])
		return B
def make_zip(f,num_files,compressed_size):
	L=num_files;T=[3988292384]+[1<<A for A in range(31)]+[1<<32];e=[E(T,A)for A in[1<<A for A in range(32)]+[(1<<32)+1]];F={0:2,1:3,2:3,18:1};M=K(F);G={97:2,256:2,285:1};N=K(G);H={0:1};U=K(H);A=S();A.push(1,1);A.push(2,2);A.push(max(G)+1-257,5);A.push(max(H)+1-1,5);V=16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15;W=max((V.index(A)for A in F))+1;A.push(W-4,4)
	for g in V[:W]:A.push(F.get(g,0),3)
	def X(E):
		B=0
		for (C,D) in sorted(E.items()):
			n=C-B
			while n>=11:
				if n<138:G=n
				elif n<149 and F[18]<(n-138)*F[0]:G=n-11
				else:G=138
				A.push_rev(*M[18]);A.push(G-11,7);n-=G
			while n>0:A.push_rev(*M[0]);n-=1
			A.push_rev(*M[D]);B=C+1
	X(G);X(H);B=0;A.push_rev(*N[97]);B+=1;i=A.bit_pos%2==0;B+=(8-A.bit_pos+1)//2*258;Y=A.bytes();A=S()
	if not i:A.push(*U[0])
	while A.bit_pos+G[285]+H[0]+G[256]<=8:A.push_rev(*N[285]);A.push(*U[0]);B+=258
	A.push_rev(*N[256]);Z=A.bytes();a=compressed_size-len(Y)-len(Z);B+=a*1032;j=b'\x00'*a;k=Y+j+Z;b=B;D=[1<<A for A in range(33)]
	for l in range(8):D=[E([T,e][97>>l&1],A)for A in D]
	O=[1<<A for A in range(33)]
	while B>0:
		if B&1:O=[E(O,A)for A in D]
		D=[E(D,A)for A in D];B>>=1
	P,B,m=k,B,O;Q=[];C=0;c=E(m,8589934591)&4294967295^4294967295;n=C
	try:C+=f.write(J('<LHHHHHLLLHH',67324752,20,0,8,27808,1352,c,len(P),b,1,0)+b'0')
	except error:raise ValueError('Please choose size of 15Kb or more')
	C+=f.write(P);d=C
	for o in Q:C+=f.write(o.serialize(zip64=0))
	for I in range(L):
		R=[]
		while True:
			R.insert(0,b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[I%36]);I=I//36-1
			if I<0:break
		C+=f.write(J('<LHHHHHHLLLHHHHHLL',33639248,20,20,0,8,27808,1352,c,len(P),b,len(bytes(R)),0,0,0,0,0,n)+bytes(R))
	p=C-d;C+=f.write(J('<LHHHHLLH',101010256,0,0,len(Q)+L,len(Q)+L,p,d,0));return C
