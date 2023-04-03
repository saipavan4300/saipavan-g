def outer_fun():
    print("outer function")
    def inner_fun():
        print("inner function")
    return inner_fun
ret_val=outer_fun()
#print(ret_val)
#print(type(ret_val))
ret_val()

