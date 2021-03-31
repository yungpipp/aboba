s=open('f.txt','r')
import random
a={}
r=5
for line in f:
    tmp=line.replace("\n","").split(" ")

    n=tmp[0]
    a[n]=[]
    for i in range(1,len(tmp)):
        rr=int(tmp[i])
        a[n].append(rr)
for n in a:
    print(n,end=":\t")
    for i in range(len(a[n])):
        print (a[n][i],end=' ')
    print('')
m=int(input('Нажмите 1, чтобы вывести всех учеников'
            ' '
            'Нажмите 2, чтобы вывести отличников'
            ' '
            'Нажмите 3, чтобы вывести двоечников'
            ' '
            'Нажмите 4, чтобы добавить ученика'
            ' '
            'Нажмите 5, чтобы удалить ученика'
            ' '
            'Нажмите 6, чтобы изменить данные ученика'
            ' '
            'Нажмите 7, чтобы выйти'))
if m==2:
    fl=True
    for n in a:
        for i in range(len(a[n])):
            if a[n][i]!=5:
                fl=False
        if fl==True:
            print(n)

if m==3:
    flag=False
    for n in a:
        for i in range(len(a[n])):
            if a[n][i]==2:
                flag=True
        if flag==True:
            print(n)