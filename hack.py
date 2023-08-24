#hack ???

import csv


with open("D:/2.csv") as f: # f=open("D:/3.csv")
    reader=csv.reader(f)
    for row in reader:
        name=row[0]
        ramz=row[1]
        dic=(name,ramz)
        print (dic)
    
