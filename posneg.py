#Write a Python program that accepts a number from the user and checks whether the number is positive, negative, or zero using if-elif-else.
a=int(input("Enter a number"))
if a>0:
    print(a,"is positive")
elif a<0:
    print(a,"is negative")
else:  print(a,"is zero")
