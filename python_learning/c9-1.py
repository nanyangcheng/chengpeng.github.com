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

class Icecreamstand(Restaurant):

    def __init__(self,restaruant_name,curisine_type='ice_cream'):
        super().__init__(restaruant_name,curisine_type)
        self.flavors = []
    
    def show_flowers(self):
        for flover in self.flavors:
            print(flover.title())

class User():

    def __init__(self,firstname,lastname,sex):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex

    def describle_user(self):
        print(self.firstname.title()+self.lastname+" is "+self.sex)

class Admin(User):

    def __init__(self,firstname,lastname,sex):
        super().__init__(firstname,lastname,sex)
        self.privilges = Privileges()


class Privileges():

    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_Privileges(self):
        for privilege in self.privileges:
            print(privilege)






a = Admin('cheng','peng','male')
a.privilges.privileges = ['can do a','ni az djf']
a.privilges.show_Privileges()
a.describle_user()
print("\n")
big_onr = Icecreamstand('The big One')
big_onr.flavors=['a','a','d','t']
big_onr.show_flowers()
big_onr.describle_restaruant()           
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