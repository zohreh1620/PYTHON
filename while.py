#Iteration
#يعني يه کاري را تا يه زماني انجام بده
#----------------------------------------------
#while

#while expression:
#      statements
#      ...
#      ...

#statement


#example1
chocolate=5
total_chocolate=chocolate

while(chocolate>0):
   print("I ate the chocolate", total_chocolate-chocolate)
   chocolate-=1

print("I ate all of them")



#example2
#the sqare root
number=float(input("give me the number"))
guess=number/2
error=0.01
iteration=0
while(abs(number -guess**2)>error):
     iteration+=1
     taghsim=number/guess
     guess=(taghsim+guess)/2

print("the square of",number,"is", guess, "iteration", iteration)


#example3
name=input("give me yor name ")
while name!='zohreh':
      print("your name in not zohreh")
      name=input("give me yor name ")

print("congradulation")


#example4
n=3
while(n>=0):
   print(n)
   n+=1
   if n==100:
      print("you reached 100")
      break

#\Pass-------------------------------------------------
#Example5
   number=10
   while number>0:
      if number%2!=0:
         pass
      else:
         print(number)
      number-=1


#Continue-----------------------------------------------
#Example6
   number=10
   while number>0:
      if number%2!=0:
         number-=1
         continue  # برگشت به حلقه ي اول براي تکرار
         print(number)
      number-=1
      

   
      
