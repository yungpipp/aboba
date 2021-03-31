s=open('s.txt','r')
import random
students=[]
r=5
for line in s:
    tmp=line.replace("\n","").split(" ")
    student = {}
    student["name"] = tmp[0]
    student['fam']=tmp[1]
    student['ot']=tmp[2]
for n in a:
    print(n)
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
            'Нажмите 7, чтобы выйти'
            ' '))
if m==1:
    print(a)
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
if m==7:
    break