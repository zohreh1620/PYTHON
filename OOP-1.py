class person:
    count=0   #class variable
    def __init__(self,name,age):
        self.name=name #object variable
        self.age=age
        person.count+=1
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def gete_info(self):
        print(self.name,self.age)
    def birthday(self):
        self.age=self.age+1
        print("happyyy")
    def return_count(self):
        return(person.count)

jadi=person('jadi',39) #object1
jadi.get_name()
jadi.get_age()
jadi.gete_info()
jadi.birthday()


zohreh=person("Zohreh", 52) #object2
zohreh.gete_info()

mary=person("mary", 75)#object3
mary.gete_info()

print("I have objects:", jadi.return_count())