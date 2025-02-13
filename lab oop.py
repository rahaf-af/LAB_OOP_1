class panda:
    def__init__(self,name:str,age:int,ginder:str,weigt:float):  

    self.name=name
    self.age=age
    self.ginder=ginder     
    self.weigt=weigt
#دالة لعب الباندا
    def play(self):
        print("{} is playing".format(self.name))
# دالة فحص الباندا الطبي
    def  being_examined(self,docName):
        print("{} is being examined by {}".format(self,docName))

from panda import panda

pandaNum1=panda("pinky",3,"female",50.43)
pandaNum2=panda("mj",4,"male",60.87)
pandaNum3=panda("joly",2,"female",30.79)
pandaNum4=panda("miky",5,"male",60.83)

print(pandaNum1.name)
print(pandaNum2.name)
print(pandaNum3.name)
print(pandaNum4.name)

pandaNum1.play()
pandaNum1.being_examined("lisa")

pandaNum2.play()
pandaNum2.being_examined("mari")

pandaNum3.play()
pandaNum3.being_examined("mike")

pandaNum4.play()
pandaNum4.being_examined("brandon")
