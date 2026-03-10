'''a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=int(input("Enter a third number"))
if a>b and a>c:
  print(a,"is bigger than")   
elif b>a and b>c:
  print(b,"is bigger than")   
elif c>a and c>b:
  print(c,"is bigger than") 
else:  print("invalid input") '''
#Write a Python program using nested if statements to find the largest among three numbers entered by the user
# Python program to find the largest among three numbers using nested if

# Take input for the three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Use nested if statements to compare numbers
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

# Display the largest number
print(f"The largest number is: {largest}")
