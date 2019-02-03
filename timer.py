# -*- coding: utf-8 -*-
import tkinter
import main
run = True; s=0; m=0; h=0

class mainWindow:
    def __init__(self,alltime,t1,t2,t3,t4):
        '''print('!!!!!!!!!!',self.t1)
        if self.t1[2]=='0' and self.t1[3]=='0' and self.t1[4]=='0':
            self.t1=int(self.t1)*1000
        elif self.t1[2]=='0' and self.t1[3]=='0':
            self.t1=int(self.t1)*100
        elif self.t1[2]=='0':
            self.t1=int(self.t1)*10
        else:
            self.t1=int(t1)'''
        self.t1=t1
        self.t2=t2
        self.t3=t3
        self.t4=t4
        self.alltime=alltime
        self.mainWindow1()
    def mainWindow1(self):
        root = tkinter.Tk()
        root.title('Добро пожаловать в методы оптимизации')
        root.geometry('750x500+100+50')
        root.resizable(False, False)
        canvas = tkinter.Canvas(root, width=750, height=500, bg='#002')
        canvas.pack()
        def Run():
            global run, s, m, h

            canvas.delete('all')

            canvas.create_text(375, 50, text='ВРЕМЯ ОТСЛЕЖИВАНИЯ', fill='white', justify='center', width=600, font=15)
            canvas.create_text(65, 160, text='время обрабатывания  целевой функции', fill='white', anchor=tkinter.SW, width=600, font=15)
            canvas.create_text(65, 180, text='время обрабатывания  ограничений', fill='white', anchor=tkinter.SW, width=600, font=15)
            canvas.create_text(65, 200, text='время вычисления точек деления', fill='white', anchor=tkinter.SW, width=600, font=15)
            canvas.create_text(65, 220, text='время вычисления значений функции в точках', fill='white', anchor=tkinter.SW,width=600, font=15)
            canvas.create_text(490, 470, text='время работы всей программы', fill='white',justify='center', width=600, font=15)
            canvas.create_text(475, 160, text=str(self.t1)+' с', fill='white',anchor=tkinter.SW, width=600, font=15)
            canvas.create_text(475, 180, text=str(self.t2)+' с', fill='white',anchor=tkinter.SW, width=600, font=15)
            canvas.create_text(475, 200, text=str(self.t3)+' с', fill='white',anchor=tkinter.SW, width=600, font=15)
            canvas.create_text(475, 220, text=str(self.t4)+' с', fill='white',anchor=tkinter.SW, width=600, font=15)
            if s!=59:
                canvas.create_text([645, 470], text="%s:%s:%s" % (h, m, s), fill='white', font=15)
                s += 1
            elif m == 59 and s==59:
                canvas.create_text([645, 470], text="%s:%s:%s" % (h, m, s), fill='white', font=15)
                h += 1
                m = 0
                s = 0
            else:
                canvas.create_text([645, 470], text="%s:%s:%s" % (h, m, s), fill='white', font=15)
                m += 1
                s = 0
            canvas.after(1000, Run)
        canvas.after(1, Run())


        global s, m, h
        s = self.alltime
        if s<=59:
            s = self.alltime
        else:
            s=self.alltime%60
            print(s)
            m=(self.alltime//60)%60
            h=self.alltime//3600
        def exit():
            root.destroy()
        but1 = tkinter.Button(root,text="Закрыть программу",command=exit,font=15)
        but1.bind('<Button-1>')
        but1.place(x=300, y=400)
        '''def new():
            root.destroy()
            main.main()
        but1 = tkinter.Button(root,text="Подсчитать заново",command=new,font=15)
        but1.bind('<Button-1>')
        but1.place(x=370, y=200)'''
        root.mainloop()

if __name__ == "__main__":
    app = mainWindow(3601,1,2,3,4)