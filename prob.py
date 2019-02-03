import time
from threading import Thread

def sec():
    i = 0
    while True:
        time.sleep(1)
        i += 1
        print(i//3600,(i//60)%60,i%60,sep=':')
        if i==10:
            break


def func2():
    i = 0
    while True:
        time.sleep(1)
        i += 1
        print(i//3600,(i//60)%60,i%60,sep=':')

if __name__ == '__main__':
    a=Thread(target = sec)
    b=Thread(target = func2)
    a.start()
    b.start()
    a.join()
    b.join()