# -*- coding: utf-8 -*-
import tkinter
import poluchfunk
import time
tt=0
class mainWindowogr:
    mas2 = []
    param=0
    def __init__(self):
        self.mainWindow3()
    def mainWindow3(self):
        root = tkinter.Tk()
        root.title('Добро пожаловать в методы оптимизации')
        root.geometry('200x200+100+50')
        root.resizable(False, False)
        canvas = tkinter.Canvas(root, width=1020, height=620, bg='#002')
        canvas.pack()
        canvas.create_text(100, 10, text='Граничные условия', fill='white', width=600, font=15)
        canvas.create_text(100, 40, text='Пример', fill='white', width=600, font=15)
        canvas.create_text(100, 60, text='2.3,4', fill='white', width=600, font=15)
        def butCallback():
            for letter in ' abcdefgihjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ!@#$%^&=;%:?<>\\*/+()\"\'':
                if letter in entry.get():
                    canvas.create_text(170, 90, text='Ошибка!', fill='white', width=600, font=("", 9))
                    return
            if entry.get()=='':
                canvas.create_text(170, 90, text='Ошибка!', fill='white', width=600, font=("", 9))
                return
            start_time = time.time()
            self.mas2.append(entry.get())
            global tt
            tt = (time.time() - start_time)
            root.destroy()
            #poluchfunk.mainWindowfunk.mainWindow2.root.destroy()


        but1 = tkinter.Button(root,
                              text="ОК",
                              command=butCallback)
        but1.bind('<Button-1>')
        but1.place(x=20, y=110)
        def entry_delete2():
            entry.delete(first=0, last='end')

        but4 = tkinter.Button(root,
                              text="Очистить", command=entry_delete2)
        but4.bind('<Button-1>')
        but4.place(x=80, y=110)
        '''def butCallback2():
            root.destroy()
            param=1

        but2 = tkinter.Button(root,
                              text="Назад",
                              command=butCallback2)
        but2.bind('<Button-1>')
        but2.place(x=20, y=150)'''
        entry=tkinter.Entry(root)
        entry.place(x=20, y=80)
        root.grab_set()
        root.focus_set()
        root.mainloop()

if __name__ == "__main__":
    app = mainWindowogr()
    print(app.mas2)