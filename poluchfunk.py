# -*- coding: utf-8 -*-
import tkinter
import poluchogr
import time
tt=0
bezogran=[]

def time2():
    return poluchogr.tt
class mainWindowfunk:
    mas = []
    def __init__(self):
        self.mainWindow2()
    def mainWindow2(self):
        root = tkinter.Tk()
        root.title('Добро пожаловать в методы оптимизации')
        root.geometry('750x500+100+50')
        root.resizable(False, False)
        canvas = tkinter.Canvas(root, width=750, height=500, bg='#002')
        canvas.pack()
        canvas.create_text(200, 40, text='Условная оптимизация', fill='white',width=600,font=15)
        canvas.create_text(180, 170, text='Введите функцию вида \'x**2+5*x\'', fill='white', width=600, font=2)
        canvas.create_text(580, 40, text='Безусловная оптимизация', fill='white', width=600, font=15)
        canvas.create_text(540, 160, text='Введите функцию вида \'(x-5)**2\'', fill='white', width=600, font=2)
        canvas.create_text(527, 180, text='Если x<0, функция вида \'(-х)\'', fill='white', width=600, font=2)
        canvas.create_text(210, 250, text='Количество вычислений', fill='white', width=300, font=15)
        canvas.create_text(570, 250, text='Количество вычислений', fill='white', width=300, font=15)
        canvas.create_line(385,0,385,380,width=1,fill='white')
        canvas.create_line(0, 380, 750, 380, width=1, fill='white')

        entry = tkinter.Entry(root, bd=3, width=40)
        entry.place(x=50, y=200)
        def butCallback():
            s=len(entry.get())-1
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\\'\"':
                if letter in entry.get():
                    canvas.create_text(340, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\*/+-()\'\"':
                if letter in n.get():
                    canvas.create_text(340, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            if entry.get()[0]=='+' or entry.get()[0]=='-' or entry.get()[0]=='*' or entry.get()[0]=='/':
                canvas.create_text(340, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                return
            if entry.get()[s]=='+' or entry.get()[s]=='-' or entry.get()[s]=='*' or entry.get()[s]=='/':
                canvas.create_text(340, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                return
            for i in range(len(entry.get())-1):
                if entry.get()[i]=='+' and entry.get()[i+1]=='+' or entry.get()[i]=='-' and entry.get()[i+1]=='-' or entry.get()[i]=='/' and entry.get()[i+1]=='/' or entry.get()[i]=='x' and entry.get()[i+1]=='x':
                    canvas.create_text(340, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            if entry.get()=='' or n.get()=='':
                canvas.create_text(340, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                return
            start_time = time.time()
            self.mas.append(entry.get())
            self.mas.append(n.get())
            root.destroy()
            global tt
            tt = (time.time() - start_time)
            self.mas+=poluchogr.mainWindowogr().mas2

            #self.mas.append(poluchogr.mainWindowogr().mas2)
        def entry_delete():
            entry.delete(first=0, last='end')
            n.delete(first=0, last='end')


        n = tkinter.Entry(root,bd=3,width=10)
        n.place(x=50, y=240)
        but3 = tkinter.Button(root,
                              text="Очистить", command=entry_delete)
        but3.bind('<Button-1>')
        but3.place(x=235, y=270)

        but1 = tkinter.Button(root,text="Решить уравнение",command=butCallback)
        but1.bind('<Button-1>')
        but1.place(x=50, y=270)

        def butCallback2():
            s=len(in2.get())-1
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\\'\"':
                if letter in in2.get():
                    canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\\'\"*/+-()':
                if letter in n2.get():
                    canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\\'\"*/+-()':
                if letter in in3.get():
                    canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\\'\"*/+-()':
                if letter in n3.get():
                    canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            if in2.get()[0]=='+' or in2.get()[0]=='-' or in2.get()[0]=='*' or in2.get()[0]=='/':
                canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                return
            if in2.get()[s]=='+' or in2.get()[s]=='-' or in2.get()[s]=='*' or in2.get()[s]=='/':
                canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                return
            for i in range(len(in2.get())-1):
                if in2.get()[i]=='+' and in2.get()[i+1]=='+' or in2.get()[i]=='-' and in2.get()[i+1]=='-' or in2.get()[i]=='/' and in2.get()[i+1]=='/' or in2.get()[i]=='x' and in2.get()[i+1]=='x':
                    canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                    return
            if in2.get()=='' or n2.get()=='' or in3.get()=='' or n3.get()=='':
                canvas.create_text(700, 210, text='Ошибка ввода!', fill='white', width=600, font=("", 9))
                return
            start_time = time.time()
            self.mas.append(in2.get())
            self.mas.append(n2.get())
            self.mas.append('')
            global bezogran
            bezogran.append(int(in3.get()))
            bezogran.append(int(n3.get()))
            root.destroy()
            global tt
            tt = (time.time() - start_time)

        def entry_delete2():
            in2.delete(first=0, last='end')
            n2.delete(first=0, last='end')
            in3.delete(first=0, last='end')
            n3.delete(first=0, last='end')


        in2=tkinter.Entry(root,bd=3,width=40)
        in2.place(x=410, y=200)
        n2=tkinter.Entry(root,bd=3,width=10)
        n2.place(x=410, y=240)
        in3=tkinter.Entry(root,bd=3,width=10)
        in3.place(x=410, y=280)
        canvas.create_text(535, 290, text='Начальная точка', fill='white', width=300,font=("", 10))
        n3=tkinter.Entry(root,bd=3,width=10)
        n3.place(x=595, y=280)
        canvas.create_text(680, 290, text='Шаг', fill='white', width=300, font=("", 11))

        but4 = tkinter.Button(root,
                              text="Очистить", command=entry_delete2)
        but4.bind('<Button-1>')
        but4.place(x=595, y=330)
        but2 = tkinter.Button(root,
                              text="Решить уравнение",
                              command=butCallback2)
        but2.bind('<Button-1>')
        but2.place(x=410, y=330)


        def exit():
            root.destroy()
        but5 = tkinter.Button(root,
                              text="Закрыть программу",
                              command=exit)
        but5.bind('<Button-1>')
        but5.place(x=315, y=400)
        root.mainloop()

if __name__ == "__main__":
    app = mainWindowfunk()
    print(mainWindowfunk.mas)
    print(bezogran)
