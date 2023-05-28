import mysql.connector as c
class axis_bank_june23:
    
    def __init__(self):
        
        self.con=c.connect(host="localhost",user="root",passwd="root1997",database="bank")
        if self.con.is_connected():
            print("Successfully connected")
            
            
    def create_table(self):
        query="create table if not exists june_2024(customer_id int primary key ,customer_name varchar(20)\
        ,account_type varchar(20),contact int,opening_bal int,closing_bal int)"
        cursor=self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        
    def insertion_value(self):
        customer_id=int(input("enter customer_id"))
        customer_name=input("enter customer_name")
        account_type=input("enter account_type")
        contact=int(input("enter contact"))
        opening_bal=int(input("enter opening_bal"))
        closing_bal=int(input("closing_bal"))
        
         
        query="insert into june_2024 values ({},'{}','{}',{},{},{})".format(customer_id,customer_name,account_type,contact,opening_bal,closing_bal)
        cursor=self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("1.continue\n 2.exit")
        k=int(input("enter your choice"))
        if k==2:
            exit


    def rectify_amt(self):
        custumer_name=input("enter name")
        custumer_id=int(input("enter customer_id"))
        query="update june_2024 set customer_name='{}' where customer_id={}".format(customer_name,customer_id)
        cursor=self.con.cursor()
        cursor.execute(query)
        if cursor.rowcount>0:
            print("its_updated")
        else:
            print("not update")
        self.con.commit()




    def erase_detail(self):
        customer_name=input("enter name")
        query="delete from june_2024 where customer_name='{}'"
        cursor=self.con.cursor()
        cursor.execute(query)
        if cursor.rowcount>0:
            print("Successfully deleted")
        else:
            print("Not deleted")
        self.con.commit()




    def display_detail(self):
        query="select * from june_2024"
        cursor=self.con.cursor()
        cursor.execute(query)
        data=cursor.fetchall()
        print(data)    
##main
o=axis_bank_june23()

while True:
    print("axis_bank_june24")
    print("1.create_table")
    print("2.insertion_value")
    print("3.rectify_amt")
    print("4.erase_detail")
    print("5.display_detail")
    print("6.Exit")
    d=int(input("choose_data"))
    if d==1:
        o.create_table()


    if d==2:
        o.insertion_value()

    if d==3:
        o.rectify_amt()

    if d==4:
        o.erase_detail()

    if d==5:
        o.display_detail()

    if d==6:
        break



    



