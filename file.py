#File  
#handle -> open, read, write, close    f.read()

#f=open("filename")
#   \n (enter)


f=open('D:/1.txt')


counter=sum=0
for line in f:
   counter+=1
   print('line number %i is: %s' %(counter, line))
   print(line.strip())
   this_number=int(line.strip())
   sum=sum+this_number
   print(sum)

   

f=open('D:/1.txt', 'w')
f.write('2333')
f.close()

#exec(open(filename).read())

#exec(open('').read())

#------------------------------------------
#------------------------------------------
#CSV (Comma Seprated Values)

import csv
import math
from statistics import mean


with open('D:/2.csv') as f:   # f=open()  f.read()  csv.reader(f)  f.close()
   reader=csv.reader(f)
   for row in reader:
      #print (row)
      name=row[0]
      #print(name)
      these_grades=list()
      for grade in row[1:]:
         these_grades.append(int(grade))
         #print(name,grade, these_grades)
      print(name, mean(these_grades))
 
       
