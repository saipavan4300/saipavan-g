print("stmt-1")
try:
    print(9/3)
    print("excuted")
except ZeroDivisionError:
    print(10/2)
print("stmt-3")

try:
    print("try")
    print(10/5)
except:
    print("except")
else:
    print("else")
finally:
    print("final")
