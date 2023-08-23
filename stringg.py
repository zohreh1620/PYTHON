#String

a='salam'
# 's' in 'salalm'  -> True      # a=='salam'  -> True
# 'a' > 'b' -> False            # 'A' >'a' -> False

#print(a[0]) #print(a[4]) #print( a[:3]) #print( a[1:3]) #print( a[3:]) #print( a[-1])
a=a+a[1:]
print(a)

#print(len(a))
#---------------------------
for i in range (0, len(a)):
    print(i, a[i])
    print(a[-1])
#---------------------------
for letter in 'my string':
    print (letter)
#---------------------------
string="abbaas"
counter=0
for i in string:
    if i=='a':
       counter+=1
print("counter of a is :", counter)
#--------------------------------------------------------------
#type('hello') -> class 'str'
#کلاسها متدهايي دارند مثل فانکشن ها

#dir('jadi')
# upper,lower, find, strip, starttswith,count  


#'jadi'.upper()
#'salammm'.cont('m')
#--------------------------------------------------------------

name='zohreh'
sen='15'
print('hello %s chetori misuni %s salete' %(name, sen))
