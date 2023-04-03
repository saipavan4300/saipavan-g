class employee:
    def __init__(self):
        self.eno=100
        self.name='tony'
        self.esal=100000
e=employee()
print(e.__dict__)
print(e.name)

class test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=test()
t.m1()
print(t.__dict__)

class test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=test()
t.m1()
t.d=40
print(t.__dict__)

