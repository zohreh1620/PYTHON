#while

#while expression:
#      statements
#      ...
#      ...

#statement


chocolate=5
total_chocolate=chocolate

while(chocolate>0):
   print("I ate the chocolate", total_chocolate-chocolate)
   chocolate-=1

print("I ate all of them")



#the suare root
number=float(input("give me the number"))
guess=number/2
error=0.01
iteration=0
while(abs(number -guess**2)>error):
     iteration+=1
     taghsim=number/guess
     guess=(taghsim+guess)/2

print("the square of",number,"is", guess, "iteration", iteration)
