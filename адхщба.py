"""

n=int(input('n='))
for i in range(n,1,-1):
    for j in range(i):
        print('*',end='')
    print('')

for i in range(1,n+1,1):
    for j in range(i):
        print('*',end='')
    print('')

"""

"""

n=5
for i in range(n):
    for j in range(n):
        if i+j<=n-1 and i<=j or i+j>=n-1 and i>=j:
            print('*',end='')
        else:
            print(' ',end='')
    print('')

"""





"""

x=int(input('x='))
if x%2:
    print('нечетное')

else:
    print('четное')

"""

"""
x=0
import random
max=0
max1=0
n=5
S=1
list=[]
for i in range(n):
    list.append(random.randint(1,5))


for i in range(n):
    if list[i]>max:
        max=list[i]
for i in range(n):
    if list[i]>max1 and max!=list[i]:
        max1=list[i]



print(max)
print(max1)



print(list)
"""


"""
for i in range(len(list)):
    S*=list[i]
print(S)




    if list[i]<max:
        max=list[i]
print(max)

"""

"""

import random
list=[]
list1=[]
S=0


n=int(input('x='))
for i in range(n):
    for j in range(n):
        list1.append(random.randint(1,5))
    list.append(list1)
    list1=[]
print(list)
for j in range(n):
    for i in range(n-1):
        if list[i][0]>list[i+1][0]:
            for k in range(n):
                list2.append(list[i][k])
            for k in range(n):
                list[i][k]=list[i+1][k]
            for k in range(n):
                list[i+1][k]=list2[k]
        list2=[]
print(list)

"""

"""
for i in range(n):
    for j in range(n):
        S+=list[i][j]
print(S)
"""

"""
import random
n=int(input('n='))
k=0
fact=1
while n>1 :
    fact*=n
    n-=1

print(fact)
"""


"""
n=int(input('n='))
s=0
while n>0:
    x=n%10
    s+=x
    n=int(n/10)
print(s)
"""

"""
n=int(input('n='))
e1=1
e2=1
k=1
while n>k:
    s=e1+e2
    e1=e2
    e2=s
    k+=1
print(e1)
"""

"""
n=int(input('n='))
fact=1
def verNi(n,fact):
    fact=1
    k=0
    while k<n:
        k+=1
        fact=fact*k
    return fact
print(verNi(n,fact))
"""

"""
n=int(input('n='))
def ache(n):
    s=0
    while n:
        s+=n%10
        n//=10
    return s
print(ache(n))
"""
"""

n=int(input('n='))
def notfun(n):
    if n in (1,2):
        return 1
    return notfun(n-1)+notfun(n-2)
print(notfun(n))

"""

"""
str=input('')
for i in range(len(str)):
    print(str[i],end='')
"""

"""
s = 'nothing  absolutely'
for i in range(len(s)):
    if s[i]==' ' and s[i+1]==' ':
        s.replace(s[i-1],'')
print(s)
"""

"""
m=12
h=45
t=50
s=h+t
if m<10:
    m='0'+str(m)
if s<10:
    s='0'+str(s)



print(m,':',s)
"""
"""
n=int(input('n='))
for i in range(n):
    for j in range(n):
        if i+j<=n-1 and i<=j or i+j>=n-1 and i>=j:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
"""

"""
n=int(input('n='))
while n%2==0:
    n=int(input('n='))


"""





"""

n=int(input('n='))
for i in range(n,1,-1):
    for j in range(i):
        print('*',end='')
    print('')

for i in range(1,n+1,1):
    for j in range(i):
        print('*',end='')
    print('')

for i in range(n):
    for j in range(n):
        print(' ',end='')
    print('')
"""


"""
s = 0
n=int(input('n='))
for i in range(n,1,-2):
    for j in range(s):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print('')
    s+=1

for i in range(1,n+1,2):
    for j in range(s):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print('')
    s-=1
"""

"""
s=0
n=int(input('n='))
while n>0:
    s+=n
    n=int(input('n='))
print(s)
"""

"""
import random
r=random.randint(0,50)
n=int(input('n='))
while n!=r:
    if n<r:
        print('r больше')
    else:
        print('r меньше')
    n=int(input('n='))
print('угадал')
"""


"""
a=12345
while a>0:
    b=a%10
    c=a//10
    d=c%10
    e=c//10
    f=e%10
    j=e//10
    h=j%10
    k=j//10
    l=k%10
    s=b+d+f+h+l
    print(s)
"""

"""
a=12345
s=1
while a>0:
    s=(a%10)*s
    a=a//10
    print(s)
"""

"""
a=int(input('a='))
s=0
s1=0
p=0
while a>0:
    if p<3:
        s+=(a%10)
        a=a//10
        print(s)
    if p>3:
        s1+=(a%10)
        a=a//10
        print(s1)
    p+=1
if s==s1:
    print('равны')
else:
    print('неравны')
"""

"""
n=int(input('n='))
fact=1
while n>1:
    fact*=n
    n-=1
if n==0:
    print(fact)
print(fact)
"""

"""
n=int(input('n='))
e1=1
e2=1
k=1
while n>k:
    s=e1+e2
    e1=e2
    e2=s
    k+=1
print(e1)
"""

"""
import random
n=int(input('n='))
a=[]
s=0
for i in range(n):
    a.append(random.randint(0,9))
    s+=a[i]
for i in range(n):
    print(a[i],end='')
    if i<(n-1):
        print(end=',')
print('')
print(s)
"""


"""
import random
a=[]
n=int(input('n='))
for i in range(n):
    a.append(random.randint(0,9))
for i in range(n):
    print(a[i],end='')
    if i<(n-1):
        print(end=',')
print('')
min=a[0]
for i in range(n):
    if a[i]<min:
        min=a[i]
print(min)
print('')
"""

"""
import random
a=[]
b=False
k=0
s=0
ar=0
for i in range(30):
    a.append(random.randint(-10,10))
for i in range(30):

    if a[i]>-5:
        k+=1
        s+=a[i]
        b=True
ar=s/k
print(ar)
if b:
    print('че')
else:
    print('да ниче')
"""

"""
a=input()
b=True
s=0
e=len(a)-1
while s<=e:
    if a[s]==' ':
        s+=1
        continue
    if a[e]==' ':
        e-=1
        continue
    if a[s]!=a[e]:
        b=False
    s+=1
    e-=1
if b==False:
    print('не палиндром')
else:
    print('палиндром')
"""

"""
import random
a=[]
n=int(input('n='))
f=True
c=0
for i in range(n):
    a.append(random.randint(0,9))
for i in range(n):
    print(a[i],end='')
    if i<(n-1):
        print(end=',')
print('')
while f==True:
    f=False
    for i in range(n-1):
        if a[i]<a[i+1]:
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
            f=True
    print(a)



"""


"""
a="abc"
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
    print(a[i],end="")
print(b)
print('')
"""


"""
a='aaaaapppcchhhhi'
s=0
n=input('n=')
for i in range(len(a)):
    if a[i]==n:
        s+=1
print(s)
"""


'''
units=['','one','two','three','four','five','six','seven','eight','nine']
dozensu=['ten','eleven','twelve','thirteen','fourteen','fivteen','sixteen','seventeen','eighteen','nineteen']
dozens=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
hundreds=['','thousand','million']
b=' '
v=0
n=int(input('n='))
while n>0:
    tmp=n%1000
    n=n//1000
    a=n%1000
    print(tmp)
    #print(units[tmp%10])
    #print(dozens[tmp%100])
    #print(hundreds[tmp%100])
    if (tmp%100)//10==1:
        if tmp//100==0:
            b=units[tmp//100]+' '+dozensu[tmp%10]+' '+hundreds[v]+ ' ' +b
            print(b)
        else:
            b=units[tmp//100]+' hundred '+dozensu[tmp%10]+' '+hundreds[v]+ ' ' +b
            print(b)
    else:
        if tmp//100==0:
            b=units[tmp//100]+' '+dozens[(tmp%100)//10]+' '+units[tmp%10]+' '+hundreds[v]+' '+b
            print(b)
        else:
            b=units[tmp//100]+ ' hundred ' +dozens[(tmp%100)//10]+' '+units[tmp%10]+' '+hundreds[v]+ ' ' +b
            print(b)
    v+=1
'''

import random
a=[]
min=100
min_i=0
s=0
c=0
h=True
f=0
n=int(input('n='))
m=int(input('m='))
for i in range(0,n):
    b=[]
    a.append(b)
    for i in range(0,m):
        b.append(random.randint(1,5))

for i in range(0,len(a)):
    print('')
    for j in range(0,len(a[i])):
        print(a[i][j],end=" ")
print('')

"""
g=int(input('g='))
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if a[i][j]==g:
            print(a[i])

"""

for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        s+=a[i][j]
        if s<min:
            min=s
            min_i = i
    a[i].append(s)
    s=0
print('')
while h==True:
        h=False
        for i in range(0,len(a)-1):
            if a[i][len(a[i])-1]>a[i+1][len(a[i])-1]:
                c=a[i]
                a[i]=a[i+1]
                a[i+1]=c
                f+=1
                h=True
        print(f)

for i in range(0,len(a)):
    print('')
    for j in range(0,len(a[i])):
        print(a[i][j],end=" ")
print('')