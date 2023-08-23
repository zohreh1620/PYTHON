#Iteration
#for

#for iteration_var in sequence:
#    statement(s)
#    ...
#    ...

#statement

#-------------------------------------------------
#example1
books=[11,2,5,8]
for i in books:
    print(i)
print("finished")

#example2
step=5
while step>0:
    print("HELLO1")
    step-=1
print("Finished1")


#example3
for x in [1,2,3,4,5]:
    print("HELLO2")

print("Finished2")

#example4
for x in range(0,10):
    print(x,x*x)
    if x==5:
        break
