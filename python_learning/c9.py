class User():

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 

    def user_discrible(self):
        print(self.a+self.b+" is "+self.c)

    def greet_user(self):
        print("Hellow "+self.a+self.b)

my = User('cheng','peng','male')
my.user_discrible
my.greet_user
