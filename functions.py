def add_fun(a,b):
    t=a+b
    print(t)
add_fun(20,30)
add_fun(40,50)
add_fun(10,20)
def print_msg():
    print("hello,good morning")
print_msg()
print_msg()
print_msg()
#wish("good morning")
#def wish(msg):
   #print(msg)
def sub_fun(a,b):
    s=a-b
    print(s)
    #return 
ret_val=sub_fun(100,25)
print(f"result of sub is{ret_val}")
def add_sub(a,b):
    add=a+b
    sub=a-b
    return add,sub
add,sub=add_sub(67,50)
print(add)
print(sub)
def person_wish(name,wish):
    print(f"{name},{wish}")
person_wish(name="mary",wish="good morning")
person_wish(name="good night",wish="mary")
