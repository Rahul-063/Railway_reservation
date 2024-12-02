import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="Rahul@*123456",database="RAILWAY_RESERVATION")

#SIGN_IN
# def sign_in():
#     a=input("enter the Username:")
#     b=input("enter the password:")
#     s1="select user_name from user_accounts where password_1='{}'".format(b)
#     x=mydb.cursor()
#     x.execute(s1)
#     data=x.fetchone()
#     if data[0]==a:
#         print("LOGIN SUCCESSFULLY")
#         main()
#     else:
#         print("UNABLE TO LOGIN")


def sign_up():
    f=input("Enter the First_name:")
    l=input("Enter the Last_name:")
    a=input("Enter the Username:")
    b=input("enter the password:")
    c=input("enter the Re-entered password:")
    phno=input("entered the phoneNumber:")
    print('M=Male','\t','f=Female','\t','Not=applicable')
    Gen=input("Enter the Gender:")
    d=input('date:')
    o=input("month:")
    p=input("year:")
    dob=d+'/'+o+'/'+p
    age=input("enter the age:")

    if b==c:
       s2="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,phno,Gen,dob,age)
       x=mydb.cursor()
       x.execute(s2)
       data=x.fetchone()
       print("-------------------------------------------")
       print("Sign_up SUCCESSFULLY")
       print("-------------------------------------------")
       main()

    else:
        print("UNABLE TO SIGN_uP")

def sign_in():
    a=input("enter the Username:")
    b=input("enter the password:")
    s1="select user_name from user_accounts where password_1='{}'".format(b)
    x=mydb.cursor()
    x.execute(s1)
    data=x.fetchone()
    if data[0]==a:
        print("-------------------------------------------------")
        print("LOGIN SUCCESSFULLY")
        print("-------------------------------------------------")
        main()
    else:
        print("UNABLE TO LOGIN")

#functions
def Ticket_Booking():
    nm=input("Enter the Name: ")
    phno=input("Enter the Phone_Number: ")
    age=input('Enter the age: ')
    gender=input("Enter the Gender: ")
    fr=input("Enter the Starting point: ")
    to=input("Enter the Destination: ")
    date1=input("enter the date(DD): ")
    date2=input("enter the month(mm): ")
    date3=input('enter the year(yyyy): ')
    date=date1+'/'+date2+'/'+date3
    d1="insert into railway values('{}','{}','{}','{}','{}','{}','{}')".format(nm,phno,age,gender,fr,to,date)
    x=mydb.cursor()
    x.execute(d1)
    data=x.fetchone()
    print("------------------------------------")
    print("Ticket Booked Successfully")
    print("------------------------------------")
    main()

def Ticket_Checking():
    phno=input("Enter the Phone Number:")
    try:
        d2="select * from railway where phno='{}'".format(phno)
        x=mydb.cursor()
        x.execute(d2)
        dat=x.fetchone()
        dat1=list(dat)
        a=['name','phone_number','Age',"gender","starting point",'Destination',"date"]
        print(a[0],'...',dat1[0])
        print(a[1],'...',dat1[1])
        print(a[2],'...',dat1[2])
        print(a[3],'...',dat1[3])
        print(a[4],'...',dat1[4])
        print(a[5],'...',dat1[5])
        print(a[6],'...',dat1[6])
        main()
    except:
        print("error")

def Ticket_cancelling():
    phno=input("enter the Phone_number: ")
    d3="select phno from railway where phno='{}'".format(phno)
    x=mydb.cursor()
    x.execute(d3)
    day=x.fetchone()
    if day[0]==phno:
        d4='delete from railway where phno=phno'
        x=mydb.cursor()
        x.execute(d4)
        print("-----------------------------------------")
        print("ticket_cancelled successfully")
        print("-----------------------------------------")
        main()
    else:
        print('Not exit')


def Ticket_display():
    a=input('Enter the User_Name:')
    b=input("Enter the Password:")
    try:
        b1="select user_name from user_accounts where password_1='{}'".format(b)
        b2="select fname,lname from user_accounts where password_1='{}'".format(b)
        x=mydb.cursor()
        x.execute(b2)
        rah1=x.fetchall()[0]
        rah=list(rah1)
        rah=rah[0]+''+rah[1]
        x.execute(b1)
        ram1=x.fetchall()[0]
        ram=list(ram1)
        if ram[0]==a:
            g1=['First Name',"last name","phone number","gender","date of birth",'age']
            g2="select fname,lname,phno,gender,dob,age from user_accounts where password_1='{}'".format(b)
            x=mydb.cursor()
            x.execute(g2)
            dated1=x.fetchall()[0]
            dated=list(dated1)
            print(g1[0],'...',dated[0])
            print(g1[1],'...',dated[1])
            print(g1[2],'...',dated[2])
            print(g1[3],'...',dated[3])
            print(g1[4],'...',dated[4])
            print(g1[5],'...',dated[5])

        else:
            print("error")
    except:
        print("404 Error")

    



#Main Function
def main():
    while True:
        print("1.Ticket_Booking")
        print("2.Ticket_Checking")
        print("3.Ticket_cancelling")
        print("4.Ticket_display")
        print("5.Log_out")

        task=input("enter the task:")

        if task=='1':
            Ticket_Booking() 
        elif task=='2':
            Ticket_Checking()
        elif task=='3':
            Ticket_cancelling()
        elif task=='4':
            Ticket_display()
        elif task=='5':
            print("-----------------------------------------")
            print("Log_out")
            break 
        else:
            print("page not found")


#Login details
while True:
    print("WELCOME RAILWAY RESERVATION SYSTEM")
    print('1.sign_in')
    print('2.sign_up')
    print("3.Exit")

    choice=input("Enter the task yoou want to perform")

    if choice=="1":
        sign_in()
    elif choice=="2":
        sign_up() 
    elif choice=="3":
        print("thank you")
        break  
    else:
        print('ERROR')
