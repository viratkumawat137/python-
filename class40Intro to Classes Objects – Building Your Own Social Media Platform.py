
#class SocialMedia:

   # CEO =  "mark"
    #def like(self):
    #    print("Liked")                            

    #def comment(self):
     #   print("Commented") 

#a = SocialMedia()
#a.like()
#a.comment()


"""class SocialMedia:

    CEO =  "mark"
    def like(self):
        print("Liked")

    def comment(self):
        print("Commented") 
facebook = SocialMedia()
twitter = SocialMedia()
twitter.CEO = "elon musk"
print(facebook.CEO)
print(twitter.CEO) """

#a = list()

#print( type (a))

#class Test:
   # a = "" 
    #b = "" 
    #c = "" 

#a    = Test()

#print( type(a)) 

"""class car :
 color = "black"
 brand = "Rolls royce"
 milage = "3mph"

def engin(self):
 print("RR Engin")

def drive(self):
 print("driving")


def honk(self):
 print("peeeeeeee")


a = car()
b = car()

print(a.brand)
print(b.brand)

b.brand = "HONDa"
b.milage = "25mph"

print(b.brand)
print(b.milage)
a.honk()"""

"""class dog:

    species = "GS"

    def eat(self):
        self.b = 50 
        print(f"hungary right now.")

    def bark(self):
        print(self.b)
        print(f" says woof!")

a = dog()
a.eat()
a.bark() """



"""class dog:

    species = "gs"

    def constr(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def eat(self):
        self.b = 50
        print(f"hungray right now.")

    def bark(self):
        print(self.d)
        print(f"says woof!")

xyz = dog()
xyz.constr()
xyz.eat()
xyz.bark()"""


"""
class dog:

    species = "gs"

    def constr(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def eat(self):
        self.b = 50
        print(f"hungray right now.")

    def bark(self):
        print(self.d)
        print(f"says woof!")

xyz = dog()
xyz.bark()"""


#constructors

"""class dog:

    species = "gs"

    def __init__(self):
        self.age = 30
        print("bhaiya object ban gaya h.")

    def eat(self):
        self.age = 50
        print(f"hungray right now.")

    def bark(self):
        print(self.age)
        print(f"says woof!")

xyz = dog()
xyz.eat()
xyz.bark()"""

""""

class dog:

    species = "gs"

    def __init__(self, age=2):
        self.age = age
        print("bhaiya object ban gaya h.")

    def eat(self):
        print(f"hungray right now.")

    def bark(self):
        print(self.age)
        print(f"says woof!")

xyz = dog()
xyz.bark()"""

""""


class dog:

    species = "gs"

    def __init__(self, age=2):
        self.age = age
        print("bhaiya object ban gaya h.")

    def eat(self):
        print(f"hungray right now.")

    def bark(self):
        print(self.age)
        print(f"says woof!")

xyz = dog(13)
xyz.bark()"""


""""
class dog:

    species = "gs"

    def __init__(self, name="tom" ,age=2):
        self.dog_name = name
        self.age = age
        self.is_hungry = True
        

    def bark(self):
        print(f"{self.dog_name} says woof!")

    def eat(self):
        if self.is_hungry:
            print(f"{self.dog_name} is eating...")
            self.is_hungry = False

        else:
            print(f"{self.dog_name} is not hungry right now.")
            self.is_hungry = True
xyz = dog()
xyz.bark()
xyz.eat()
xyz.eat()
xyz.eat()"""

""""
class Car:

   

    def __init__(self, brand="tata", color="white"):

        self.brand =brand

        self.color = color

        self.engine_status = "off"



    def start_engine(self):

        if self.engine_status == "on":

            print(f"The{self.brand} s engine is now on.")

            self.engine_status = "off"

        else:

            print(f"The {self.brand}  s engine is now off.")

            self.engine_status = "on"    



a = Car ()

print(a.brand)

print(a.color)

a.start_engine()

print(a.engine_status)

a.start_engine()

print(a.engine_status)"""


""""class GST:
    Tax_rate =18

    def __init__(self,name):
        self.name = name
milk = GST(name="saras")
bread = GST(name="amul")

print(f"{milk.name} has {milk.Tax_rate} rate.")
print(f"{bread.name} has {bread.Tax_rate} rate.")

"""



""""class Demo:
    def __init__(self):
        pass
    def test():
        print("hi")

    def test1(self):
        print("hi")

a = Demo()
a.test()
"""


""""class bankaccount:
    bank_name = "sbi"

    def __init__(self,name,mob,age,dob,balance):
        self.name = name
        self.mob = mob
        self.age =age 
        self.dob =dob
        self.balance = balance

    def show_info(self):
        print(self.name,
              self.mob,
              self.age,
              self.balance)
        
    def deposit(self,amount):
        if amount <= 0:
            print("invalid amount")
            exit(1)
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("invalid amount" )
            exit(1) 

        self.balance -= amount

demo=bankaccount("demo",111,21,"113323", 500)
demo.deposit(100)
demo.show_info()
demo.withdraw(200)
demo.show_info()"""


