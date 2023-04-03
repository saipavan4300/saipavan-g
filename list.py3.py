l1=list(range(1,11))
print("l1: ",l1)
print("length of l1: ",len(l1))
l2=[1,1,1,2,2,4,4,9,9,9,]
print("count of 9: ",l2.count(9))
l3=[1,2,3]
print("l3: ",l3)
l3.append(99)
print("l3 after append: ",l3)
l3.insert(1,88)
print("l3 after insert: ",l3)
l3.insert(100,111)
print("l3 after insert again: ",l3)
l3.insert(-100,88)
print("l3 after insert again : ",l3)
l4=[1,2,3]
l5=[11,22,33]
print("l4: ",l4)
print("l5: ",l5)
l4.extend(l5)
print("l4 after extend: ",l4)
l6 =[11,22,33,44,55,66]
print("l6 before remove: ",l6)
l6.remove(44)
print("l6 after remove: ",l6)
l6.pop(1)
print("l6 after pop: ",l6)
l6.pop()
print("l6 after pop: ",l6)

prime_numbers=[2,3,5,7]
prime_numbers.reverse()
print("reverse list: ",prime_numbers)

l7=[12,45,6,7,8,134,6,8,768]
l7.sort()
print("l7 after sort: ",l7)
l7.sort(reverse= True)
print("l7 after sort: ",l7)

l8=['z','A','b','p','Q','d']
print("l8 before sort: ",l8)
l8.sort()
print("l8 after sort: ",l8)
l9=['Abc','B','R','Xys','Zebra']
l9.sortr()
print(l9 after sort: ",l9)
