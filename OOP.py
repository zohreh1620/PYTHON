#OOP (Object Oriented Programming)

#Object --> 

#Human (name, family, ...)-> Employee, Teacher, student, ...
#ترکيب کردن شي ها با هم
#ارث بري
#استاد ارث ميبره از کارمند ولي يه چيزاي بيشتر داره


#class
#متغير و متد

#variable -> 1-class var 2-object variable



#class person
# ....name
# ....age 



#jadi=person


#method (return name)
#---------------------------------
#کلاس درست مي کنيم. بعد ميگيم حالا از کلاس يه شي درست کن

class person:
    count=0
    def __init__(self, name, age): #method init(shoru)
        self.name=name
        self.age=age
    def get_name(self):
        print(self.name)

jadi=person('jadi', 40)




