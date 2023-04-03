a=[0,5,10,15,20]
for i in a:
    if i%2==0:
        print(str(i)+'is an even number')
    else:
       print(str(i)+'is an odd number')

l=[1,2,3,4,5]
obj=iter(l)
print(type(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
