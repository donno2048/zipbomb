# warning: minified
from struct import pack as F
from functools import reduce
G=lambda m,v:reduce(lambda i,j:i^j,[j*(v>>i&1) for i,j in enumerate(m)])
def make_zip(f,num_files,compressed_size):
	A,H,B,I,a,o=(1<<32)-1,num_files,compressed_size,[1<<A for A in range(33)],range(8),[0]*8
	for n in a:
		for b in a:o[n]=o[n]>>1^3988292384*((1<<n>>b^o[n])&1)
	C,D=B*1032-14447,o+I[:24]+[0];K=C
	while C:
		if C&1:I=[G(I,A)for A in D]
		D=[G(D,A)for A in D];C>>=1
	L=~G(I,A)&A;J=f.write(F('<QLHLLLLQLH',85966670672,8,0,L,B,K,1,36536642864,1409003712,25695)+b'\x0b'+b'\0'*(B-15)+b'`');M=J
	for E in range(H):N=str(E).encode();J+=f.write(F('<QQLLLHQQ',5629585467198288,524288,L,B,K,len(N),0,0)+N)
	f.write(F('<QHHLLH',101010256,H,H,J-M,M,0))
