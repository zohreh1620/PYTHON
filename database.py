#database MYSQL, MariaDB


#create table table_name(var1 varchar(5),var2 int,var3 float,var3 char)


#show tables
#desc table_name;


#insert into table_name VLUES (...)

#select* from table_name
#select var1 from table_name
#select var1 from table_name where ..

#--------------------------------------------
#Linux -->
#pip3 install mysql-connector-python  ???


# connect to Database
import mysql.connector
print('connecting to db')
cnx=mysql.connector.connect(user='root', password='AAAaaa123!@#',
                            host='127.0.0.1',
                            database='db_1')

print('connected to db')
cursor=cnx.cursor()
#cursor.execute("CREATE TABLE tb1 (name varchar(10))")
cursor.execute("INSERT INTO tb1 VALUES ('zohreh')")
cnx.commit()

cnx.close()

#----------------------------------------------------------------------
# Read fro database
import mysql.connector
print('select data from db')
cnx=mysql.connector.connect(user='root', password='AAAaaa123!@#',
                            host='127.0.0.1',
                            database='db_1')
cursor=cnx.cursor()
query="select * from tb1"
cursor.execute(query)
for (name) in cursor:
    print(name)
print('selected data from db')
cnx.close()

