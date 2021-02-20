import numpy as np
from matplotlib import pyplot as plt
w=np.arange(-np.pi,np.pi,0.001*np.pi)
F=100
Fs=500
x=np.random.rand(500)
#x=x-np.sum(x) for getting a constant noise
l=len(x)
X=[]
for i in range(0,len(w)):
	s=0
	for n in range(0,l):
		s=s+x[n]*np.exp(-1*1j*w[i]*n)
	X.append(s)
#plt.subplot(211)
plt.title("DTFT Magnitude Spectra")
plt.stem(w,np.abs(X))
#plt.subplot(212)
#plt.title("DTFT Phase spectra")
#plt.stem(w,np.angle(X))
plt.show()	
