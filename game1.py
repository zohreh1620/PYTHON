#game, guess the number

def game1(a,b):
   import random
   x=random.randint(a,b)
   #print(x)
   y=int(input("guess the number: "))

   while x!=y:
     if x>y:
        print("Your number is lower than x")
     else:
        print("Your number is higher than x")
     y=int(input("guess the number: "))
  
   
   print("Congradulation", x ,"==", y)
   print("****************************")


again= input("Do you want to play again ? Press 1 ")
while again=='1':
    a=int(input("Give the first range: "))
    #print (a)
    b=int(input("Give the second range: "))
    #print (b)
    game1(a,b)
    again= input("Do you want to play again ? Press 1 ")
  
        
