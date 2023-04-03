class numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
      if self.a<=20:
        x=self.a
        self.a+=1
        return x
     else:
        raise stopiteration 
number_class=numbers()
number_iter=iter(number_class)
print(type(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

      
