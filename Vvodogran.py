class ogran:
    def __init__(self,q):
        self.k=q
    def ogra(self):
        p=self.k.split(',')
        print(p)
        zz=[float(p[i]) for i in range(len(p))]
        return zz
