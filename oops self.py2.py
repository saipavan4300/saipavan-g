class test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
t=test()
t.m1()
t.m2()

class student:
    def __init__(self):
        self.a=100
    def disp(self):
        a=20
        print(self.a)
        print(a)
s=student()
s.disp()

class animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{}walks with{}legs...'.format(name,cls.legs))
animal.walk('dog')
animal.walk('cat')




