import optimization
import Noneogran
import Vvodogran
import time
t2=0
def time3():
    return optimization.t3
def time4():
    return optimization.t4
class Metody:
    def __init__(self,mas):
        self.mas=mas
    def setka(self):
        ogr=Vvodogran.ogran(self.mas)
        return ogr.ogra()


class Ogranichen:
    def __init__(self,a,b,c,x,t):
        self.a=a
        self.b=b
        self.c=c
        self.x=x
        self.t=t
    def usloptimization(self):
        masagr=optimization.ogran(self.a,self.b,self.c)
        return masagr.deserve()

    def bezuslovoptimization(self):
        start_time = time.time()
        sven=Noneogran.newogran(self.b,self.x,self.t)
        global t2
        t2 = (time.time() - start_time)
        bezuslovn=optimization.ogran(self.a,sven,self.c)
        return bezuslovn.deserve()
