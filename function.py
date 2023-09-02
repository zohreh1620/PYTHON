#function : Build in

#type() , Print(), int(), min(), max()

#------------------------------------------------------------
#function : Library

#ipmort math
#math.sin()

#import random
#random.random()      random.randint()
#------------------------------------------------------------
#function: khodeman

#def function_name(params_optional):
#    statement(s)
#    ...
#   ...

#function_name()



def function1():
    for i in range(1,5):
       print("Your number is:", i)

function1()
#------------------------------------------------------------

def function2(to_whom):
    print("Hello To ", to_whom)


function2("Zohreh")
#------------------------------------------------------------

def function_name(name):
    print("salam", name)
    print("bye", name)

function_name("JADI")
#------------------------------------------------------------
def sum(a,b):
    javab=a+b
    return javab

adade_aval=5
adade_dovom=8
jam=sum(adade_aval,adade_dovom)
print(jam)
#-------------------------------------------
def squares(*args):
    squared_args=[]
    for item in args:
        squared_args.append(item*item)
    return squared_args


print(squares(1,2,3,5))
#---------------------------------------------
#keyword arguments
def person_details(**kwargs):
    for key, value in kwargs.items():
        print(key, '->', value)
print(person_details(name='a', alias='d', job='ff'))
#-----------------------------------------------------------
#توابع بازگشتي
#-----------------------------------------------------------
#توابع پنهان
lambda_square= lambda n: n*n

print(lambda_square(4))





    
