#Fibonatchi

n1=1
n2=1

num=int(input("EnterNumber:"))
if num==1:
    print (n1)
elif num==2:
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    i=3
    while i<=num:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        i+=1
    
