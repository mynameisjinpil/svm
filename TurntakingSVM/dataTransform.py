f=open("./turntaking.txt",'r')
data=f.read().split(",")
data=map(float,data)
f.close()
x=[]
X=[]
y=[]

for i in range(len(data)):
	if (i%2==1):
		y.append(data[i])
	else:
		x.append(data[i])

X=zip(x[0::1])
y=map(int,y)

#print X
#print y

