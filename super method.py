class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
class student(person):
    def __init__(self,name,age,rollno,marks):
        super(). __init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super(). display()
        print(self.rollno)
        print(self.marks)
s1=student('mary',22,101,90)
s1.display()
