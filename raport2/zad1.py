import numpy as np
import scipy.stats as scp
import matplotlib.pyplot as plt
plik=open("./raport2/lista7zad1.txt",'r')
p=plik.read()
p=p.split(",")
N=1_000_000
for i in range(len(p)):
    p[i] = float(p[i])
#temp=np.random.choice(p,size=N,replace=True)
#p.extend(temp)
#dotąd metoda bootstrap
def check_if_between(x,a,b):
    if x>a and x<b:
        return True
    if x>a and b==None:
        return False
    if a==None and x<b:
        return True
    if a==None and x>b:
        return False


sigma=0.2
x_dash=np.mean(p)   
Z=x_dash
alpha=0.05
left_crit=(-1)*scp.norm.ppf(q=1-alpha,loc=0,scale=1)
right_crit=scp.norm.ppf(q=1-alpha,loc=0,scale=1)
both_crit=scp.norm.ppf(q=1-(alpha/2),loc=0,scale=1)
t=np.linspace(-3,3,500)
pdf_draw=[scp.norm.pdf(x) for x in t]
plt.plot(t,pdf_draw)
plt.fill_between(x=t,y1=pdf_draw,where = (t<-both_crit),color='r')
plt.fill_between(x=t,y1=pdf_draw,where = (t>both_crit),color='r')
mu=1.5
Z=(Z-mu)/(sigma/np.sqrt(len(p)))
print(Z)
#plt.show()
p_value=2*(scp.norm.sf(abs(Z)))
print(p_value)