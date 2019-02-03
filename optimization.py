#from pandas import DataFrame
import otchet
import time
import matplotlib.pyplot as plt
t3=0
t4=0
class ogran:
    def __init__(self,a,b,c):
        self.fuct=a
        self.ogr=b
        self.n=c
    def deserve(self):
        print(self.fuct)
        list(self.ogr)
        #n=(ogr[1]-ogr[0])/e
        int(self.n)
        print("n=",self.n)
        start_time = time.time()
        xx=[round(self.ogr[0]+kk*((self.ogr[1]-self.ogr[0])/int(self.n)),4) for kk in range(int(self.n))]
        print(xx)
        global t3
        t3=(time.time() - start_time)
        start_time2 = time.time()
        result=[]
        for x in xx:
            z=eval(self.fuct)
            result.append(round(z,6))
        itog={'Xi':xx,'F(Xi)':result}
        #data=DataFrame(itog)
        global t4
        t4=(time.time() - start_time2)
        #print(data)
        #rint(data['Xi','F(Xi)'][data['F(Xi)'].idxmin()])
        #print(data[['Xi','F(Xi)']][5])
        #k=data.loc[data['F(Xi)'].idxmin()]
        otchet.otchet1(xx)
        otchet.otchet2(xx,result)
       # print(data['F(Xi)'].idxmin(),k[0],k[1])
        uniqdict = dict(zip(xx, result))
        print(uniqdict)
        plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='r')
        plt.axis([-100, 100, -200, 200])

        plt.title('F(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xx, result, color='blue', linestyle='solid', label='F(x)')
        plt.grid(True)
        plt.show()
        keyy=min(uniqdict, key=uniqdict.get)
        minn=uniqdict[keyy]
        print('Минимальное значение функции ',keyy,'-',minn)
        keyymax=max(uniqdict, key=uniqdict.get)
        maxx=uniqdict[keyymax]
        print('Максимальное значение функции ', keyymax, '-', maxx)
        otchet.otchet4(minn,keyy,maxx,keyymax)

if __name__ == "__main__":
    app=ogran('(2*x**2-12*x)',[0,4],15)
    app.deserve()
