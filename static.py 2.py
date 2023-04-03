class custommath:
    @staticmethod
    def add(x,y):
        print(x+y)
    @staticmethod
    def product(x,y):
        print(x*y)
    @staticmethod
    def average(x,y):
        print((x+y)/2)
custommath.add(10,20)
custommath.product(10,20)
custommath.average(10,20)
c1=custommath()

class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        print(id(self))
        print(id(other))
        return self.pages+other.pages
b_one=book(100)
b_two=book(200)
b_three=b_one+b_two
print(id(b_one))
print(id(b_two))
print(b_three)


