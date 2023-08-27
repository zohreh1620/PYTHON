#generator // type of functions
# يادش مي ماند اطلاعات قبلي را
#جاهايي خوبه که مي خ.اهيم جوابها تند تند برگردند
#از نظر حافظه بهينه است
#زماني که نمي دونيم چقدر خروجي داريم


#function
def function():
     return(1,2,3)


#generator
def firstn(n):
    num=0
    while(num<n):
         yield num
         num+=1
    



for i in firstn(10):
      print(i)
      



    
