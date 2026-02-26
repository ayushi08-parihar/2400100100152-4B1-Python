num1=int(input("Enter your number"))     
num2=int(input("Enter your number"))
while True:
    print("^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^CHOICES^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_^^_")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        print("The sum is",num1+num2)
    elif choice==2:
        print("The difference is",num1-num2)
    elif choice==3:
        print("The product is",num1*num2)
    elif choice==4:
        if num2==0:
            print("Cannot divide by zero")
        else:
            print("The quotient is",num1/num2)
    elif choice==5:
        print("Thank you for using our calculator")
        break
    else:
        print("Invalid choice")   