#example

while True:
    num=int(input("Enter number:"))
    sum=0
    for i in range(1,num):
        if (num%i==0):
            sum+=i
    
    if (sum==num):
        print("Perfected")

    else:
        print("not Perfected")

    #answer=print("continue? Y")
    #if(answer=='Y'):
    #    continue
