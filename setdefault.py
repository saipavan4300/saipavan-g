s7={1,2,3,4}
print("s7: ",s7)
s7.add(11)
print("after updation: ",s7)

l=[1,2,3]
t=(111,222,333)
s={888,999,777}
s1=set()
s1.update(l,t,s)
print("s1: ",s1)
r_val=s1.pop()
print("r_val: ",r_val)
print("s1: ",s1)
s1.remove(777)
print("s1 after remove: ",s1)
#s1.remove(444)
s1.discard(444)
print("s1: ",s1)
s1.clear()
print("s1: ",s1)
