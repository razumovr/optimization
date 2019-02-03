# -*- coding: utf-8 -*-
def otchet(a):
    f = open('text.txt', 'w',encoding='utf-8')
    f.write('Эта программа предназначена для нахождения максимального или минимального значения целевой функции однокритериальной зада-\nчи условной (безусловной) оптимизации.\n')
    for index in a:
        if index==a[2]:
            f.write('Заданный промежуток:'+'['+str(index)+']'+'\n')
        elif index==a[0]:
            f.write('Целевая функция: ')
            f.write(str(index)+'\n')
        else:
            f.write('Количество вычислений: ')
            f.write(str(index)+'\n')
    f.close()
def otchetsven(a):
    f = open("text.txt", "r",encoding='utf-8')
    lines = f.readlines()
    f.close()
    f = open("text.txt", "w",encoding='utf-8')
    for line in lines:
        if line != 'Заданный промежуток:[]\n':
            f.write(line)
    f.close()
    f = open('text.txt', 'a',encoding='utf-8')
    f.write('Заданный промежуток: ')
    f.write(str(a) + '\n')
    f.close()
    #print(lines)
def otchet1(b):
    f1 = open('text.txt', 'a',encoding='utf-8')
    f1.write('Точки деления: ')
    f1.write('[ ')
    for index in b:
            f1.write(str(index)+' ')
    f1.write(']\n')
    f1.close()
def otchet2(x,r):
    f2 = open('text.txt', 'a',encoding='utf-8')
    f2.write('Значения функции f(x) в точках деления:\n')
    f2.write('{0:>7}{1:>13}\n'.format('Xi','F(Xi)'))
    number=range(1,len(x)+1)
    for index0,index1,index2 in zip(number,x,r):
        f2.write('{0:5}{1:10}{2}\n'.format(str(index0),str(index1),str(index2)))
    f2.close()
def otchet4(a,b,c,d):
    f2 = open('text.txt', 'a',encoding='utf-8')
    f2.write('Минимальное значения функции на заданном промежутке F(Xi)= '+str(a)+' в точкe Xi= '+str(b)+'\n')
    f2.write('Максимальное значения функции на заданном промежутке F(Xi)= ' + str(c) + ' в точкe Xi= ' + str(d) + '\n')
    #f2.write(str(a) + '\n')
    #f2.write(str(b) + '\n')
    f2.close()
def otchet3(a,b,c,d):
    f3= open('text.txt', 'a',encoding='utf-8')
    f3.write('время обрабатывания целевой функции: '+str(a) +' сек' + '\n'+'время обтабатывания ограничений: '+ str(b)+' сек'   + '\n'+'время вычисления точек деления: '+ str(c)+' сек' + '\n'+'время вычисления значений функции в точках: '+ str(d)+' сек' + '\n')
    f3.close()

if __name__ == "__main__":
    otchet(['stroka',122,'lol'])