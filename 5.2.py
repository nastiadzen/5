class Student:
    def __init__(self, name, settings_dict):
        self.name=name
        self.a=settings_dict['a']
        self.b=settings_dict['b']   
        self.c=settings_dict['c']      
        self.d=settings_dict['d']  
        self.e=0       
        self.f=0      
        self.g=[]     
        for i in range(self.c):self.g.append(dict(h=0, j=None))
    def passLabWork(self, j, k):
        if j>self.b:
            try:
                self.g[k]['tryCount']+= 1
                self.g[k]['mark']=j
                return True
            except IndexError:
                return False
        else:
            return False
    def passIndWork(self, j):
        if j > self.a:
            self.f+=1
            self.l=j
            return True
        else:
            return False