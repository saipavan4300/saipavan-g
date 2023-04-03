from functools import reduce
num_list=[10,20,30,40,50]
add_result=reduce(lambda x,y:x*y,num_list)
print(add_result)
def fun_print():
    print("Hello")
print(fun_print)
print(id(fun_print))
print(type(fun_print))
