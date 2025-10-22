class calculator:
    def add(self,a,b,c=0,*args):
        print(a+b+c+sum(args))
    


a = calculator()
a.add(2,2)
a.add(2,2,2)
a.add(2,2,2,2,2)