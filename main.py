from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="85898589",database="python_db")
"""
if con:
    print("connect")
else:
    print("error")
"""
def insert(name,age,city):
    res=con.cursor()
    qry="insert into users(name,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    res.execute(qry,user)
    con.commit()
    print("datas inserted")

def update(name,age,city,id):
    res = con.cursor()
    qry = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(qry, user)
    con.commit()
    print("datas  updataed")

def select():
    res=con.cursor()
    qry="select id,name,age,city from users"
    res.execute(qry)
    result=res.fetchall() #fetch- use to how many row shoud be  print the condition
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))#tabulate-this one package use to tables format printed
    print("datas selected")


def delete(id):
    res=con.cursor()
    qry="delete from users where id=%s"
    user=(id,)
    res.execute(qry,user)
    con.commit()
    print("the datas  is deleted")
msg="""
      1.insert data
      2.update data
      3.select data
      4.delete data
      5.exit 
     """
while True:
    print(msg)
    ch=int(input("enter your choice:"));
    if ch==1:
        print ("insert your datas:")
        name=input("enter your name:")
        age=int(input("enter your age:"))
        city=input("enter your city:")
        insert(name,age,city)
    elif ch==2:
        print("update your datas:")
        id=int(input("enter your id:"))
        name = input("enter your name:")
        age = int(input("enter your age:"))
        city = input("enter your city:")
        update(name, age, city,id)
    elif ch==3:
        print("selce your datas:")
        select()
    elif ch==4:
        print("delete your datas:")
        id=int(input("enter your id:"))
        delete(id)
    else:
        print("thank you")
        quit()



