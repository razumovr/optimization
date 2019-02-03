import time
import otchet
def newogran(func,a,b):
    start_time = time.time()
    x0=a
    t=b
    k=0
    #print(x0)
    intervall=[]
    func0=[eval(func) for x in [x0-t,x0,x0+t]]
    #print(func0)
    if func0[0]>=func0[1]<=func0[2]:
        interval=[x0-t,x0+t]
        print(interval)
        intervall.append(interval)
    elif func0[0]<=func0[1]>=func0[2]:
        print("Function is not unimodal")
        return
    elif func0[0]>=func0[1]>=func0[2]:
        delta=t
        a0=x0
        x1=x0+t
        k=1
        interval=[a0]
        sk = 0
        while sk != 1000:
            xnext = x1 + 2**k*delta
            funcxnet=func.replace('x',str(xnext))
            funcx1 = func.replace('x', str(x1))
            if eval(funcxnet)<eval(funcx1):
                interval.pop()
                interval.append(x1)
                x1=xnext
                k=k+1
                sk += 1
                continue
            elif eval(funcxnet)>=eval(funcx1):
                interval.append(xnext)
                break
        print(interval)
        intervall.append(interval)
    elif func0[0]<=func0[1]<=func0[2]:
        delta=-t
        b0=x0
        x1=x0-t
        k=1
        interval=[b0]
        sk=0
        while sk!=1000:
            xnext = x1 + 2**k*delta
            funcxnet=func.replace('x',str(xnext))
            funcx1 = func.replace('x', str(x1))
            counter=0
            if eval(funcxnet)<eval(funcx1):
                interval.pop()
                interval.append(x1)
                x1=xnext
                k=k+1
                counter+=1
                sk += 1
                continue
            elif eval(funcxnet)>=eval(funcx1):
                interval.insert(0, xnext)
                break
        print(interval)
        intervall.append(interval)
    otchet.otchetsven(intervall[0])
    t2 = (time.time() - start_time)
    #print("T2----------",t2)
    return sum(intervall,[])

if __name__ == "__main__":
    newogran('x**3',1,1)
    #newogran('(x)**4+8*(x)**3-6*(x)**2-72*(x)')