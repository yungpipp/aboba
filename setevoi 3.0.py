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
    student['group']=tmp[3]
    student['marks']={}
    for i in range(4,len(tmp),2):
        student["marks"][tmp[i]]=int(tmp[i+1])
    students.append(student)
m=0
while m!=7:
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
        print(students)
    if m==2:
        for student in students:
            fl=True
            for i in student['marks']:
                if student['marks'][i]!=5:
                    fl=False
            if fl==True:
                print(student)

    if m==3:
        for student in students:
            fl=False
            for i in student['marks']:
                if student['marks'][i]!=2:
                    fl=True
            if fl==False:
                print(student)
    if m==4:
        student = {}
        student["name"]=input('Введите имя: ')
        student['fam']=input('Введите фамилию: ')
        student['ot']=input('Введите отчество: ')
        students.append(student)
        print('Ученик добавлен, проверьте список учеников')
    if m==5:
        num=int(input('Введите номер ученика, которого хотите удалить: '))
        students.pop(num)
        print('Ученик удален, проверьте список учеников')
    if m==6:
        numb=int(input('Введите номер ученика, чьи данные хотите изменить: '))
        iz=input('Какие данные Вы хотите изменить? (Пишите с заглавной буквы) ')
        if iz=='Имя':
            students[numb]["name"]=input('Введите имя: ')
        if iz=='Фамилия':
            students[numb]["fam"]=input('Введите фамилию: ')
        if iz=='Отчество':
            students[numb]["ot"]=input('Введите отчество: ')
        if iz=='Группа':
            students[numb]['group']=input('Введите группу: ')
        if iz=='Оценки':
            izz=input('Вы хотите добавить или удалить оценку? ')
            if izz=='Добавить':
                pr=input('Введите название предмета: ')
                students[numb]['marks'][pr]=int(input('Укажите оценку: '))
            if izz=='Удалить':
                pr=input('Введите название предмета: ')
                del students[numb]['marks'][pr]





print('Вы вышли')
exit()
