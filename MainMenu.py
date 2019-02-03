# -*- coding: utf-8 -*-
import tkinter
import poluchfunk
def bezorg():
    return poluchfunk.bezogran
def time1():
    return poluchfunk.tt
def time2():
    return poluchfunk.time2()
class mainWindow:
    def __init__(self):
        self.mainWindow1()
        self.allargument = poluchfunk.mainWindowfunk.mas
    def mainWindow1(self):
        root = tkinter.Tk()
        root.title('Добро пожаловать в методы оптимизации')
        root.geometry('750x500+100+50')
        root.resizable(False, False)
        canvas = tkinter.Canvas(root, width=750, height=500, bg='#002')
        canvas.pack()
        canvas.create_text(375, 50, text='Эта программа предназначена для нахождения максимального или минимального значения целевой функции однокритериальной задачи условной (безусловной) оптимизации.', fill='white',justify='center',width=600,font=15)


        def butCallback():
            root.destroy()
            poluchfunk.mainWindowfunk()

        but1 = tkinter.Button(root,
                              text="Начать",
                              command=butCallback,font=15)
        but1.bind('<Button-1>')
        but1.place(x=375, y=350)
        def butCallback2():
            root.destroy()

        but2 = tkinter.Button(root,
                              text="Закрыть",
                              command=butCallback2,font=15)
        but2.bind('<Button-1>')
        but2.place(x=650, y=450)
        root.mainloop()

if __name__ == "__main__":
    app = mainWindow()
    print(poluchfunk.mainWindowfunk.mas)
