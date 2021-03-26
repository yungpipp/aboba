a={}
import random
h=int(input('Кол-во учеников: '))
r=int(input('Кол-во оценок: '))

for i in range(h):
    n=input('Имя ученика: ')
    a[n]=[]
    for i in range(r):
        rr=random.randint(2,5)
        a[n].append(rr)
for n in a:
    print(n,end=":\t")
    for i in range(len(a[n])):
        print (a[n][i],end=' ')
    print('')
m=int(input('Нажмите 1, чтобы вывести отличника'
            ' '
            'Нажмите 2, чтобы вывести двоешника'
            ' '))
if m==1:
    for n in a:
        for i in range(len(a[n])):
            if a[n][i]==4 or a[n][i]==5:
                print(n)

if m==2:
    for n in a:
        for i in range(len(a[n])):
            if a[n][i]==2 or a[n][i]==3:
                print(n)