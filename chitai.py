import random
f=open('f.txt','w')
n=int(input('n='))
for i in range(1,n):
    f.write(str(i))
    f.write('\n')
f.write(str(n))
f.close()

f=open('f.txt','r')
for a in f:
    print(int(a)*2)
