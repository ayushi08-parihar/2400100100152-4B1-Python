#Write a Python program to reverse a number entered by the user using a while loop.
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10
print("The reversed number is:", reverse)
