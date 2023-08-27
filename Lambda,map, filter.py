#Programming

#Lambda Function

#يکبار مصرف
#anonymos
#lambda arg:expression


lambda x:x*2
myfunc= lambda x:x*2

myfunc(3)
print (myfunc(3))


#---------------------------
a=[(3,4),(7,1),(5,9),(2,2)]
a.sort()
print(a)

#sort based on the second argument
a.sort(key=lambda x:x[1])
print(a)

#-------------------------
#map (fuction ra be dune dune map mikonim  map(fun, mylist)
 
mylist=[1,3,4,2,0.5]
map(lambda x:x*2, mylist)
print(list(map(lambda x:x*2, mylist)))


numbers=[10,11,8,5,4]
map(lambda x:'big' if x>10 else 'small', numbers)
print(list(map(lambda x:'big' if x>10 else 'small', numbers)))

#-------------------------
#Filter   filter(fun,list)

list2=[5,6,8,9,10,45]
filter(lambda x:x%2==0 , list2)
print(list(filter(lambda x:x%2==0 , list2)))
