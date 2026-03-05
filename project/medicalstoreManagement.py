import mysql.connector as myc

cn=myc.connect(host="localhost",user="root",passwd="ayu",database="Medical")#Change
mycursor=cn.cursor()

def menu():
    while True:
        cho=int(input('''
1.Show all the medicines
2.Search for a medicine
3.Buy a medicine
4.Show medicines I bought
5.Drop a medicine from my basket
6.Amount I have to pay
7.Exit

Enter your choice(1-6):'''))

        if cho==1:
            mycursor.execute("Select * from medicine;")

            data=mycursor.fetchall()
            for row in data:
                print("Medcine code:",row[0])
                print("--------------------------------------")
                print('Medine name:',row[1])
                print("--------------------------------------")
                print("Medicine for:",row[2])
                print("--------------------------------------")
                print("Medicine price:",row[3])
                print("--------------------------------------")
        elif cho==2:
            med_code=int(input("Enter medicine code you want to search:"))
            val=(med_code,)
            mycursor.execute("Select * from medicine where med_code=%s",val)
            
            if mycursor.fetchone() is None:
                print("Sorry the searched medicine is not available in the store")

            else:
                mycursor.execute("Select * from medicine where med_code=%s",val)
                data=mycursor.fetchall()
                for row in data:
                    print("Medcine code:",row[0])
                    print("--------------------------------------")
                    print('Medine name:',row[1])
                    print("--------------------------------------")
                    print("Medicine for:",row[2])
                    print("--------------------------------------")
                    print("Medicine price:",row[3])
                    print("--------------------------------------")

        elif cho==3:
            med_code=int(input("Enter medicine code you want to buy:"))
            val=(med_code,)
            mycursor.execute("Select * from medicine where med_code=%s",val)
            
            
            if mycursor.fetchone() is None:
                print("Sorry the searched medicine is not available in the store")
            else:
                mycursor.execute("Select * from medicine where med_code=%s",val)
                data=mycursor.fetchall()
                med_name=data[0][1]
                price=data[0][3]
                qty=int(input("Enter quantity of medicine you want to buy:"))
                Tup=(username,med_code,med_name,qty,price,qty*price)                #med_code,med_name,qty,med_price)
                mycursor.execute("Insert into buyy values(%s,%s,%s,%s,%s,%s)",Tup)
                cn.commit()
                print("Medicine successfully added in the basket")

        elif cho==4:
            name=input("Enter your name:")
            val=(name,)
            mycursor.execute("select * from buyy where buyer_name=%s;",val)
            data=mycursor.fetchall()
            for row in data:
                print("Buyer Name:",row[0])
                print("--------------------------------------")
                print('Medicine Code:',row[1])
                print("--------------------------------------")
                print("Medicine Name:",row[2])
                print("--------------------------------------")
                print("Quantity:",row[3])
                print("--------------------------------------")
                print("Medicine price:",row[4])
                print("--------------------------------------")
            
        elif cho==5:
            name=input("Enter your name:")
            med_code=input("Enter medicine code you want to drop from your basket:")
            
            val=(name,med_code)
            mycursor.execute("Select * from buyy where buyer_name=%s and med_code=%s",val)
            
            if mycursor.fetchone() is None:
                print("Sorry the searched medicine is not available in the store")

            else:
                name=input("Enter your name:")
                med_code=input("Enter medicine code you want to drop from your basket:")
                val=(name,med_code)
                mycursor.execute("DELETE FROM BUYY WHERE buyer_name=%s and med_code=%s",val)
                cn.commit()
                print("Successfully Dropped")

        elif cho==6:
            name=input("Please enter your name:")
            val=(name,)
            mycursor.execute("Select sum(Total) from buyy where buyer_name=%s",val)
            data=mycursor.fetchall()
            Total=data[0][0]

            print("You have to pay:",Total)

        elif cho==7:
            print("Thankyou for visiting")
            print("Log Out")
            break
        else:
            print("Invalid CHoice")





while True:
    ch=int(input('''
1.LOGIN
2.CREATE ACCOUNT
3.EXIT

Enter choice:'''))

    if ch==1:
        username=input("Enter username:")
        print("--------------------------------------")
        passwrd=int(input("Enter ypur 4-Digit password:"))
        print("--------------------------------------")

        val=(username,passwrd)
        mycursor.execute("Select * from user_table where username=%s and password=%s",val)

        if mycursor.fetchone() is None:
            print("INVALID USERNAME AND PASSWORD")
            print("TRY AGAIN")
        else:
            print("Welcome To the medical store")
            print("##############################################################")
            menu()

    elif ch==2:
        username=input("Enter username:")
        print("--------------------------------------")
        passwrd=int(input("Enter ypur 4-Digit password:"))
        print("--------------------------------------")

        val=(username,passwrd)
        mycursor.execute("Insert into user_table values(%s,%s)",val)
        cn.commit()
        menu()
    elif ch==3:
        if cn.is_connected():
            cn.close()
        print("Thankyou")
        break
    else:
        print("Invalid Choice")
#Table Details:

#user_table(username char(25) primary key,password int(4));
#medicine(med_code int(3) primary key,med_name char(25),Used_for chaer(20),med_price int(5));
#buyy(buyer_name char(25),med_code int(3),med_name char(25),qty int(3),med_price int(5),Total int(8));
