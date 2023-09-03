#example


aval=0
dovom=0
for i in range(0,20):
    #id=input("ID:")
    moadel=float(input("Average:"))
    if (moadel>aval):
             dovom=aval
             aval=moadel
             
    elif  moadel>dovom:
        
        dovom=moadel

    print("moadel:",moadel,"aval:",  aval,"dovom:",dovom)
  
    
