a={}
h=int(input('кол-во ком '))
r=int(input(''))

for i in range(h):
    n=input('название ')
    a[n]=[]
    for i in range(r):
        rr=int(input())
        a[n].append(rr)
for n in a:
    print(n,end=":\t")
    for i in range(len(a[n])):
        print (a[n][i],end=' ')
    print('')