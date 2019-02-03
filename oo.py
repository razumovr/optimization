from pandas import DataFrame
import timer
from threading import Thread
def func1():
    i = 0
    while True:
        timer.sleep(1)
        i += 1
        print(i//3600,(i//60)%60,i%60,sep=':')

def func2(a0,b1,cn):
    p1 = Thread(target=func1)
    p1.start()
    x=[b1[0]+kk*((b1[1]-b1[0])/int(cn)) for kk in range(int(cn))]
    #x = [self.ogr[0] + kk * ((self.ogr[1] - self.ogr[0]) / int(self.n)) for kk in range(int(self.n))]
    print(x)
    result = []
    for i in x:
        z = eval(a0)
        result.append(z)
    itog = {'Xi': x, 'F(Xi)': result}
    data = DataFrame(itog)
    print(data)
    return x
class ogran:
    def __init__(self,a,b,c):
        self.fuct=a
        self.ogr=b
        self.n=c
    def deserve(self):
        list(self.ogr)
        print(self.ogr)
        #n=(ogr[1]-ogr[0])/e
        int(self.n)
        print("n=",self.n)
        #p1 = Thread(target=func1)
        x = Thread(target=func2, args=(self.fuct, self.ogr, self.n))
        x.start()
        #p1.start()
        #x.join()
        #p1.join()



'''def func1():
  print 'func1: starting'
  for i in xrange(10000000): pass
  print 'func1: finishing'

def func2():
  print 'func2: starting'
  for i in xrange(10000000): pass
  print 'func2: finishing'

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p1.join()
  p2.join()'''