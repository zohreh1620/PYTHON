#List


my_list=['h',7,6,'b']

#avali
my_list[0]
print(my_list)
print(my_list[0])

my_list[0]=12
print(my_list[0])

#akhari
print(my_list[-1])

print(my_list[-2])

print(type(my_list))
#-------------------------------
#فقط جمع و ضربدر يک عدد
l1=[5,3,2]
l2=[0,'g','k']
l3=l1+l2
l4=l1*3



#Method of Lists------------------------------------------------
#فانکشنهايي که روي آبجکتها تعريف مي شوند

#object --> dog
#method --> dog.run()

new_list=[1,4,6,3,66,9,6]

#sort
new_list.sort()
print(new_list)


#Sorted
a=sorted(new_list)

#insert
new_list.insert(4,55)
print(new_list)

#append
new_list.append('tah')
print(new_list)

#extend(list)
new_list.extend([6,44,33])

#remove
new_list.remove(6)
print(new_list)

#delete
del (new_list[4])

#pop
#از ته برميدارد
new_list.pop()
print(new_list)

#اولي را برميدارد
new_list.pop(0)


#index
new_list.index(6)

#count
new_list.count(55)

#reverse
new_list.reverse()


#Slicing----------------------------------------------------------
#list[startindex:endindex]

my_list=[1,2,3,5,8,'dog',7,8,88,'pig']

my_list[0:3]
my_list[:3]
print(my_list)

my_list[2:5]
print(my_list)

my_list[0:-1]
print(my_list)

my_list[-3:-1]
print(my_list)


my_list[-3:-1]
print(my_list)

list=[6,7,4]
my_list=[list, 5,57,[1,'e'], 90]
print("my list is :", my_list)


#list[startindex:endindex:step]

my_list[3:5:2]
print(my_list)


my_list[3:5:]
print(my_list)

my_list[3:5:2]
print(my_list)

my_list[3:]
print(my_list)
#-------------------------------------------------------
#max(my_list)
#min(my_list)
#sum(my_lit)

len1=len(my_list)
print(" len my_list is:", len1)
for i in range(0, len(my_list)):
    print(my_list[i])
#-------------------------------------------------------
#split
s='some words are here'
print(s.split())
print(s.split('a'))
# '-".join(s)
#-------------------------------------------------------
#aliasing

a='123'
b='123'
#a is b ->True

a=[1,2]
b=[1,2]
#a is b -> False


a=[1,2,3]
b=a
#a is b ->True
