"""1. Найти площадь, ограниченную линиями
1в y=x**2-4; y=5-x**2
2в y=2x-x**2; x+y=0"""
def f(x):
    return x**2-2*x-3
def g(x):
    return -2
def HDM(a,b,e,f):
	arr=[]
	for i in range(a,b):
		a=i
		b=i+1
		c = 0
		while(a<=b-e and c<10000):
			h=0
			if f((a+b)/2)*f(b)==0:
				if (a+b)/2==0:
					arr.append((a+b)/2)
					break
				else:
					arr.append(b)
					break
			elif f((a+b)/2)*f(b)<0:
				a=(a+b)/2
				h=1
			elif f(a)*f((a+b)/2)<0:
				b=(a+b)/2
				h=1
			c+=1
		if(h==1):
			arr.append(a)
	return arr
def e(x):
    return f(x)-g(x)
def sq(f,a,b,e):
    s=0
    while a<=b-e:
        s+=f(a)*e
        a=a+e
    return s

y=HDM(-20,20,0.001,e)
print(y)
if(len(y))==2:
    print(abs(sq(f,y[0],y[1],0.001)-sq(g,y[0],y[1],0.001)))
else:
    print("Фигура не замкнута!")