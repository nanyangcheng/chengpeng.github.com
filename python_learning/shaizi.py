from random import randint
class Die():

    def __init__(self,number,sider=6):
      self.sider = sider
      self.number = number

    def roll_die(self):
        for x in range(0,self.number):
            y = randint(1,self.sider)
            print(y)

shaizi = Die(10)
shaizi.roll_die()
print("\n")
shai = Die(10,100)
shai.roll_die()

