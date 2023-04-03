class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def disp_info(self):
        print(self.name)
        print(self.roll_no)
s1=student("ram",101)
s1.disp_info()
s1=student("john",101)
s1.disp_info()
            
