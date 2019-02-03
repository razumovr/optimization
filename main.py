import Metodoptimization
import grafinterface
import otchet
import timer
import time
def main():
    start_time = time.time()
    arguments=grafinterface.Graf().mainarguments
    if arguments[2]!='':
        otchet.otchet(arguments)
        ogr=Metodoptimization.Metody(arguments[2])
        a1=Metodoptimization.Ogranichen(arguments[0],ogr.setka(),arguments[1],0,0)
        a1.usloptimization()
        alltime=int(time.time() - start_time)
        print(alltime)
        time1=round(grafinterface.time1(),6)
        time2=round(grafinterface.time2(),6)
        time3=round(Metodoptimization.time3(),6)
        time4=round(Metodoptimization.time4(),6)
        #print(grafinterface.time1())
        #print(grafinterface.time2())
        #print(Metodoptimization.time3())
        #print(Metodoptimization.time4())
        timer.mainWindow(alltime,time1,time2,time3,time4)
        otchet.otchet3(time1,time2,time3,time4)
    #elif arguments[2]>10**100:
        #print("Вы ввели не унимодальную функцию,запустите заново программу")
    else:
        otchet.otchet(arguments)
        a2=Metodoptimization.Ogranichen(arguments[0],arguments[0], arguments[1],grafinterface.bezorg()[0],grafinterface.bezorg()[1])
        a2.bezuslovoptimization()
        alltime=int(time.time() - start_time)
        print(alltime)
        time1=round(grafinterface.time1(),6)
        time2=round(Metodoptimization.t2,6)
        time3=round(Metodoptimization.time3(),6)
        time4=round(Metodoptimization.time4(),6)
        #print(grafinterface.time1())
        #print(Metodoptimization.t2)
        #print(Metodoptimization.time3())
        #print(Metodoptimization.time4())
        timer.mainWindow(alltime,time1,time2,time3,time4)
        otchet.otchet3(time1, time2, time3, time4)
if __name__ == "__main__":
    main()
#i**4+8*i**3-6*i**2-72*i