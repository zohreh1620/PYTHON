#Nested Loops


#even numbers
#for i in range(2,50):
#    if (i%2==0):
#       print ("this number is even", i)



#prime numbers between 2 and 50      

this_number=2
while(this_number<51):
    is_prime_number=True
    counter=2
    while(counter<this_number-1):
        if((this_number%counter)==0):
            is_prime_number=False
        counter+=1
    if (is_prime_number):
            print(this_number)
            
    this_number+=1


this_number=2
for this_number in range(2,51):
     is_prime_number=True
     for counter in rage(2,this_number):
        if(this_number %counter ==0):
            is_prime_number=False
            break
          
     if (is_prime_number):
        print(this_number)
    
