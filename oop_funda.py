


# ************************************************************

# Bike assinment is in this file 



# # class User:
# #     pass

# # michael = User()
# # anna  = User()

# # print(michael,anna)


# class User:
#     def __init__(self,name,email,num):
#         self.name = name
#         self.email = email
#         self.logged = False 
#         self.level = num
#     def login(self):
#         if self.logged == True:
#             print(self.name + "has just logged in." + "Welcome " + self.name + "!!!")
#         return self
#     def leveled(self):
#         if self.level > "3":
#             print(self.name + " your level is " + self.level)
#         return self
# new_user1 = User("Ash", "ash@codingdojo.com", "5")
# new_user2 = User("Folami", "folami@coingdojo.com", "9")
# # print(new_user.name, new_user.email, new_user.level)
# new_user1.login().leveled()
# new_user2.login().leveled()

# # class User:
# #     name="Anna"
# # anna = User()
# # print("anna's name:", anna.name)                            
# # User.name = "Bob"
# # print("anna's name after change:", anna.name)               
# # bob = User()
# # print("bob's name:", bob.name)                              

# ********************************************************************
# ********************************************************************
# ********************************************************************
# ********************************************************************
# ********************************************************************

# bike assignment below

# ********************************************************************
# ********************************************************************
# ********************************************************************
# ********************************************************************
# ********************************************************************
# ********************************************************************








class Bike:
    def __init__(self, name, price, speed, miles):
        self.name = name
        self.price = price
        self.speed = speed
        self.miles = miles

    def displayinfo(self):
        print(f"My Bike is {self.name}  price tag of {self.price} has speed {self.speed} and it's mileage is {self.miles} ")
        return self
    def riding(self):
        self.miles = self.miles + 100
        print(f"riding and my new mileage is {self.miles}")
        return self
    def reversing(self):
        self.miles = self.miles - 200
        if self.miles < 0:
            self.miles = 0
        print(f"reversing and my new mileage is {self.miles}")
        return self

bike1 = Bike("Raptor", "$6500", "220mph", 300)
bike2 = Bike("Night-Hawk", "$7500", "230mph", 780)
bike3 = Bike("Ninja", "$5500", "180mph", 220)

bike1.riding().riding().riding().reversing().displayinfo()
bike2.riding().riding().reversing().reversing().displayinfo()
bike3.reversing().reversing().reversing().displayinfo()
bike3.reversing().reversing()



