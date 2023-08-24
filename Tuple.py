#Tuple
#simmilat to list but they are immutable (nemishavad tagheer dad)

#list []
#dictionary {}
#tuple ()

#-------------------------
t=(1,2,3, 'hello')
#type(t) -> class 'tuple'
t[0]
t[1:3]

#t[0]=45   -> nemishavad tagheer dad

tt=tuple()


a=[1,2]
x,y=a
#x->1  y=2

x,y=4,5
#x->4  y=5
#------------------
email='aaa@gmail.com'
email.split('@')
name,domain=email.split('@')
#-----------------------

#dictionary

vazn={'jadi': 52, 'ali': 56, 'zohreh': 54}
print(vazn.items())
list(vazn.items())

for name, vazn in list(vazn.items()):
    print ('vazn %s is %s' % (name, vazn))

#-----------------------


phone=dict()
phone['jadi']='0912'
#phone -> {'jadi':'0912'}
phone['jadi', 'home']='0912'
#phone -> {('jadi','home'): '0912', 'jadi': '0912}
print(phone)



