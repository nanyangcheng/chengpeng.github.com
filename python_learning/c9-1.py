class Restaurant():

    def __init__(self,restaruant_name,curisine_type):
        self.restaruant_name = restaruant_name
        self.curisine_type = curisine_type
        self.number_served = 0

    def ser_number_served(self,number):
        if number > self.number_served:
            self.number_served = number
        else:
            print(" You can not do this")

    def increment(self,finger):
        self.number_served += finger

    def describle_restaruant(self):
        print(self.restaruant_name+"is openning")
        print(self.curisine_type)
        
    def open_retaranut(self):
        print("this is "+self.restaruant_name)

class User():

    def __init__(self,firstname,lastname,sex):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex

    def describle_user(self):
        print(self.firstname.title()+self.lastname+" is "+self.sex)


            
peo = User('cheng','peng','male')
res = Restaurant('cheng','peng')
peo.describle_user()
print(res.number_served)
res.increment(100)
res.increment(100)
res.ser_number_served(10)
print(res.number_served)
print(res.curisine_type+res.restaruant_name)
res.describle_restaruant()