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