class Computer:
    count=0 #class variable
    def __init__(self, ram,hard,cpu): #Constructor method
        Computer.count+=1
        self.ram=ram
        self.hard=hard
        self.cpu=cpu

    def value(self):
        return self.ram+self.cpu+self.hard
    def __del__(self): #mokhareb
         Computer.count-=1



    
pc1=Computer(10,5,4)
pc2=Computer(20,5,4)
pc3=Computer(30,5,4)
del pc2
print(pc1.value(), pc3.value())



# laptop az Computer ersbari mikonad, 
class Laptop(Computer): #Inheritence  # bayad hatman az haman init Computer estefade konim
        def value(self):    #overload ya Overwrite kardane function
             return self.ram+self.cpu+self.hard+self.size
        pass

laptop1=Laptop(40,5,4)
laptop1.size=5
laptop2=Laptop(50,5,4)
laptop2.size=6
print(laptop1.value(),laptop2.value())
