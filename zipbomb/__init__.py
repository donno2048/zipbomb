# warning: minified
from struct import pack as F
from functools import reduce
G=lambda m,v:reduce(lambda i,j:i^j,[j*(v>>i&1) for i,j in enumerate(m)])
def make_zip(f,num_files,compressed_size):
	A,H,B,I=(1<<32)-1,num_files,compressed_size,[1<<A for A in range(33)];C,D=B*1032-14447,[1996959894,3993919788,124634137,249268274,498536548,997073096,1994146192,3988292384]+[1<<A for A in range(24)]+[A+1];K=C
	while C:
		if C&1:I=[G(I,A)for A in D]
		D=[G(D,A)for A in D];C>>=1
	L=G(I,2*A+1)&A^A;J=f.write(F('<LLLHLLLLLLLH',67324752,20,8,0,L,B,K,1,2176904496,8,1409003712,25695)+b'\x0b'+b'\0'*(B-15)+b'`');M=J
	for E in range(H):N=str(E).encode();J+=f.write(F('<LLLLLLLHLLLL',33639248,1310740,524288,0,L,B,K,len(N),0,0,0,0)+N)
	f.write(F('<LLHHLLH',101010256,0,H,H,J-M,M,0))
