class p:
    def m1(self):
        print("p method")
class p2:
    def m2(self):
        print("p2 method")
class c(p,p2):
    def m3(self):
        print("child method")
c=c()
c.m1()
c.m2()
c.m3()
