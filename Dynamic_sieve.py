def crible_dEra(n):
	P = [True for i in range(0,n+1)]
	P[0]=False;P[1]=False 
	for i in range(2,n//2 + 1):
		if(P[i]==False):
			continue
		c = 2 
		while(c*i<=n):
			P[c*i]=False 
			c+=1 
	return P 
P = crible_dEra(10**6)
def euler_toient(n):
	phi = n
	k = 2 
	p = n 
	while(p!=1 and k*k<=p):
		if(P[k] and p%k==0):
			phi//=k;phi*=(k-1)
			while(p%k==0):
				p//=k
			k=2
		k+=1
	if(k*k>p and p!=1):
		phi//=p
		phi*=(p-1)
	return phi
t = int(input())
i = 0 
while(i<t):
	print(euler_toient(int(input())))
	i+=1
