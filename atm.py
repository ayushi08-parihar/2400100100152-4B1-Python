
//code for atm machine
balance=10000
pin=1234            
while True:
    user_pin=int(input("Enter your pin"))
    if user_pin==pin:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            print("Your balance is",balance)
        elif choice==2:
            amount=int(input("Enter amount to withdraw"))
            if amount>balance:
                print("Insufficient balance")
            else:
                balance-=amount
                print("Withdrawal successful")
                print("Your balance is",balance)
        elif choice==3:
            amount=int(input("Enter amount to deposit"))
            balance+=amount
            print("Deposit successful")
            print("Your balance is",balance)
        elif choice==4:
            print("Thank you for using our ATM")
            break
        else:
            print("Invalid choice")
    else:
        print("Incorrect pin")  


