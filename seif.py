import random
f=0
code=[0,0,0]
s=0
for i in range(len(code)):
    code[i]=random.randint(1,9)
    code[i]+=1
    if code[i]==10:
        code[i]=f
        s+=1
print(s)
print(code)