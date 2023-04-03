class Tvmodel:
    def tv_fun(self,model,operation):
        print(model)
        print(operation)
class fridgemodel:
    def fridge_fun(self,model,operation):
        print(model)
        print(operation)
tv1=Tvmodel()
fd1=fridgemodel()
tv1.tv_fun("sony","video")
fd1.fridge_fun("Bpl","cooling")
