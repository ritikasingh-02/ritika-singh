import mysql.connector
#CREATING THE DATABASE
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh")
my=mydb.cursor()
my.execute("create database if not exists Cloth")
mydb.commit()
print("database created")
my.close()
mydb.close()
#CREATING TABLE
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh",database="Cloth")
my=mydb.cursor()
my.execute("create table if not exists store(pno int,pid int,pname varchar(100),price float,stock int)")
print("table store created")
mydb.commit()
my.close()
mydb.close()
#INSERTING VALUE INTO TABLE
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh",database="Cloth")
my=mydb.cursor()
my.execute("insert into store values(101,30567,'silk chiffon dress',400000,6500)")
my.execute("insert into store values(102,30568,'polka dots and GG silk dress',370000,4000)")
my.execute("insert into store values(103,30569,'viscose rib stitch dress',170000,7000)")
my.execute("insert into store values(104,30570,'gemstone embellished fitted dress',310000,5000)")
my.execute("insert into store values(105,30571,'silk viscose jumsuit with cuffs',447000,4000)")
my.execute("insert into store values(106,30572,'checked shirts dress',340000,3000)")
my.execute("insert into store values(107,30573,'wool dress with pleats',430000,8000)")
my.execute("insert into store values(108,30574,'viscose dress with double G chain',317000,3000)")
mydb.commit()
print("values inserted")
my.close()
mydb.close()
#PROGRAM TO PERFOR ALL THE OPERATIONS ON TABLE
import mysql.connector
def menu():
    c='y'
    while c=='y':
        print(">>>>>>>>>>>>>>>WELCOME TO ORCHIDS CLOTHING STORE<<<<<<<<<<<<<<<")
        print("1.add record")
        print("2.update record")
        print("3.delete record")
        print("4.display record")
        print("5.close the program")
        choice=int(input('\nEnter your choice: '))
        if choice==1:
            adddata()
        elif choice==2:
            update1()
        elif choice==3:
            delete1()
        elif choice==4:
            display1()
        elif choice==5:
            print("\nClosing the program")
        else:
            print("\nPlease check")
        c=input("\nDo you want to continue..(y/n)")
#performing all the operations
def adddata():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh",database="Cloth")
    my=mydb.cursor()
    pno=int(input('\nEnter the product no:'))
    pid=int(input('Enter the product id:'))
    pname=input('Enter the product name')
    price=int(input('Enter the price of the product:'))
    sa=int(input('Enter the stock available:'))
    q="insert into store values({},{},'{}',{},{})".format(pno,pid,pname,price,sa)
    my.execute(q)
    mydb.commit()
    print("\nValue inserted")
    my.close()
    mydb.close()
def update1():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh",database="Cloth")
        my=mydb.cursor()
        pid=int(input("\nEnter the product id to be changed"))
        price=int(input('Enter the price to be changed'))
        q="update store set price={} where pid={}".format(price,pid)
        my.execute(q)
        mydb.commit()
        my.close()
        mydb.close()
        print("\nUpdated Successfully")
    except mysql.connector.Error as error:
        print("\nFailed to update record to database: {}".format(error))
def delete1():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh",database="Cloth")
    my=mydb.cursor()
    pid=int(input('Enter the respective product id'))
    t="delete from store where pid={}".format(pid)
    my.execute(t)
    mydb.commit()
    print("\nDeleted")
    my.close()
    mydb.close()
def display1():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="ritikasingh",database="Cloth")
    my=mydb.cursor()
    my.execute("select * from store")
    k=my.fetchall()
    for a in k:
        print(a)
        my.close()
        mydb.close()
menu()

